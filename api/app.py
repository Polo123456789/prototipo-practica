from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/hello')
def hello():
    return jsonify("Hola mundo")

if __name__ == "__main__":
    app.run()