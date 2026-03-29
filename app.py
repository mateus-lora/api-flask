from flask import Flask, request, jsonify
from services import DataService
from auth import require_api_key

app = Flask(__name__)
data_service = DataService()

@app.route('/data', methods=['POST'])
@require_api_key
def create_data():
    try:
        value = request.json.get('data')
        data_service.process_new_data(value)
        return jsonify({"message": "Valor adicionado com sucesso"}), 201
        
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/data', methods=['GET'])
@require_api_key
def fetch_data():
    try:
        values = data_service.retrieve_formatted_data()
        return jsonify(values), 200
        
    except Exception as e:
        return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)