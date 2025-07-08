import React, { useState } from "react";

const PromptChatboxPage = () => {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { sender: "ai", text: "Welcome, child. Ask your question." }
  ]);

  const handleSend = (e) => {
    e.preventDefault();
    if (!input) return;
    setMessages([...messages, { sender: "user", text: input }]);
    // Placeholder: Simulate AI reply
    setTimeout(() => {
      setMessages(msgs => [...msgs, { sender: "ai", text: `Adiyogi says: The answer to '${input}' is within you.` }]);
    }, 500);
    setInput("");
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 32 }}>
      <h2>Ask Adiyogi</h2>
      <div style={{ minHeight: 200, border: "1px solid #ccc", padding: 16, marginBottom: 16 }}>
        {messages.map((msg, idx) => (
          <div key={idx} style={{ textAlign: msg.sender === "ai" ? "left" : "right" }}>
            <b>{msg.sender === "ai" ? "Adiyogi" : "You"}:</b> {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSend} style={{ display: "flex" }}>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Ask your question..."
          style={{ flex: 1, marginRight: 8 }}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default PromptChatboxPage; 