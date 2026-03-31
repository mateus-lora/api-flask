from flask import Flask, flash, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from services import DataService
from auth import require_api_key
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chave_dev_temporaria")

data_service = DataService()

if not os.path.exists(app.instance_path):
    os.makedirs(app.instance_path)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), unique=True, nullable=False)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user")
    password = request.form.get("password")

    if user == "admin" and password == "123":
        return redirect("/tasks")
    else:
        flash("Login inválido!")
        return redirect(url_for("home"))

@app.route('/tasks')
def index():
    tasks = Tasks.query.all()
    return render_template('crud.html', tasks=tasks)

@app.route('/create', methods=["POST"])
def create_task():
    description = request.form.get('description', '').strip()

    if not description:
        return redirect('/tasks')

    existing_task = Tasks.query.filter_by(description=description).first()
    if existing_task:
        flash("Tarefa já existe!")
        return redirect('/tasks')

    new_task = Tasks(description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/tasks')

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        task.description = request.form['description']
        db.session.commit()
    return redirect('/tasks')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Tasks.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/tasks')

@app.route('/data', methods=['POST'])
@require_api_key
def create_data():
    try:
        value = request.json.get('data')
        data_service.process_new_data(value)
        return jsonify({"message": "Valor adicionado com sucesso"}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception:
        return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/data', methods=['GET'])
@require_api_key
def fetch_data():
    try:
        values = data_service.retrieve_formatted_data()
        return jsonify(values), 200
    except Exception:
        return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(host="0.0.0.0", port=5000, debug=True)