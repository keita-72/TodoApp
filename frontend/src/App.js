import React, { useEffect, useState } from "react";

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/todos")
      .then((res) => res.json())
      .then((data) => {
        console.log("取得したTODO:", data);
        setTodos(data);
      })
      .catch((err) => console.error("エラー:", err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>TODOリスト</h1>
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>{todo.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
