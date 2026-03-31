# API Flask - Camadas e Autenticação

Este repositório contém a entrega da atividade de uma aplicação Flask, aplicando boas práticas de Engenharia de Software.

## 👥 Equipe (Autores)
1. Mateus Lora - 1136218
2. Ricardo Rigo Antunes - 1136661
3. Gabriel Hanel - 1135926

## 🏗️ Arquitetura e Domínio do Código
Para melhorar a manutenibilidade, o código foi dividido em 4 responsabilidades:
* **`app.py` (Controlador):** Lida com as rotas HTTP (REST) e JSON, além de persistir os dados usando SQLAlchemy.
* **`services.py` (Regra de Negócio):** Valida os dados e formata a saída.
* **`database.py` (Camada de Dados):** Isola o banco de dados (SQLite) usando o padrão Repository.
* **`auth.py` (Autenticação):** Implementa um Decorator para proteger as rotas com API Key.

## 🚀 Como executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Na mesma pasta do projeto, crie um arquivo chamado `.env`
3. Dentro desse arquivo `.env`, escreva a seguinte linha com uma senha da sua escolha:
   `API_KEY=sua-senha-aqui`
4. Execute a aplicação: `python app.py`

## 🔒 Como testar (Funcionalidade)
No seu cliente REST (como Postman ou Insomnia), envie a requisição com o seguinte cabeçalho (header):
* Chave: `x-api-key`
* Valor: `A senha que você definiu no arquivo .env`

## Demonstração do projeto funcionando:
* Login:
![Imagem](./src/login.png)

* Colocar Tarefa:
![Imagem](./src/listaLimpa.png)

* Tarefa Salva:
![Imagem](./src/telaatividades.png)

* Tarefa Existente: 
![Imagem](./src/jaexiste.png)