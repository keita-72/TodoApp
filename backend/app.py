from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)# Flaskのアプリケーションを作成する
CORS(app)

# 仮のTodoリスト
todos = [
    {"id":1,"title":"買い物"},
    {"id":2,"title":"宿題"}
]

@app.route("/todos/<int:todo_id>",methods=["DELETE"])# ルーティングの設定
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return jsonify({"message":"削除しました"}),200

if __name__ == "__main__":
    app.run(debug=True)
