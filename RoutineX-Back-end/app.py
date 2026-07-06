from flask import Flask
from flask_cors import CORS
from flasgger import Swagger
from database import create_tables
from routes import register_routes

app = Flask(__name__)

CORS(app)
Swagger(app)

create_tables()
register_routes(app)

@app.route("/")
def home():
    return {
        "mensagem": "API Streaks funcionando!"
    }

if __name__ == "__main__":
    app.run(debug=True)


