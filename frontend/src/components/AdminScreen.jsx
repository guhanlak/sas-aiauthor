import React from "react";

const AdminScreen = () => {
  return (
    <div style={{ padding: 32 }}>
      <h2>Admin Panel</h2>
      <section>
        <h3>Upload Book</h3>
        <input type="file" accept=".txt,.pdf" />
        <button>Upload</button>
      </section>
      <section style={{ marginTop: 32 }}>
        <h3>Users</h3>
        <ul>
          <li>user1@example.com</li>
          <li>user2@example.com</li>
        </ul>
      </section>
    </div>
  );
};

export default AdminScreen; 