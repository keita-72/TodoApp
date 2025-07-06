from flask import Flask, jsonify

app = Flask(__name__)# Flaskのアプリケーションを作成する

@app.route("/api/todos")# ルーティングの設定
def get_todos():
    return jsonify([
        {"id": 1, "title": "勉強する", "done": False},
        {"id": 2, "title": "買い物に行く", "done": True}
    ])

if __name__ == "__main__":
    app.run(debug=True)
