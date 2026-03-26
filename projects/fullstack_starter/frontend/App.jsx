import { useState } from "react";

export default function App() {
  const [message, setMessage] = useState("Frontend is ready");

  return (
    <main style={{ fontFamily: "sans-serif", padding: 24 }}>
      <h1>Fullstack Starter</h1>
      <p>{message}</p>
      <button onClick={() => setMessage("Now connect this to the backend API")}>
        Next Step
      </button>
    </main>
  );
}
