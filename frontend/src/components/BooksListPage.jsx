import React from "react";

const BooksListPage = () => {
  const books = [
    { id: 1, title: "Book One", author: "Author A" },
    { id: 2, title: "Book Two", author: "Author B" },
  ];

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 32 }}>
      <h2>Books List</h2>
      <ul>
        {books.map(book => (
          <li key={book.id}>
            <strong>{book.title}</strong> by {book.author}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BooksListPage; 