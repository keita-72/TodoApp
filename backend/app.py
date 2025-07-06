from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)# Flaskのアプリケーションを作成する
CORS(app)

@app.route("/api/todos")# ルーティングの設定
def get_todos():
    return jsonify([
        {"id": 1, "title": "勉強する", "done": False},
        {"id": 2, "title": "買い物に行く", "done": True}
    ])

if __name__ == "__main__":
    app.run(debug=True)
