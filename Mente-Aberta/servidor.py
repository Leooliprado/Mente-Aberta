from flask_cors import CORS
import json
import random
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/api/assunto', methods=['GET'])
def get_random_assunto():
    with open('assuntos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        assunto = random.choice(data['assuntos'])
        return jsonify(assunto)

if __name__ == '__main__':
    app.run(host="10.0.0.179", debug=False)
