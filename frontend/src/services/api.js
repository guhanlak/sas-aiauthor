const API_URL = process.env.REACT_APP_API_URL;

export async function login(email, password) {
  // Placeholder: Call /auth/login
  return { access_token: "jwt-token" };
}

export async function register(email, password, role) {
  // Placeholder: Call /auth/register
  return { message: "User registered" };
}

export async function uploadBook(file, meta) {
  // Placeholder: Call /books/upload
  return { id: 1 };
}

export async function listBooks() {
  // Placeholder: Call /books
  return [
    { id: 1, title: "Book One", author: "Author A" },
    { id: 2, title: "Book Two", author: "Author B" },
  ];
}

export async function askQuestion(bookId, message) {
  // Placeholder: Call /chat/ask
  return { response: `Adiyogi says: The answer to '${message}' is within you.` };
}

export async function listUsers() {
  // Placeholder: Call /admin/users
  return [
    { id: 1, email: "user1@example.com" },
    { id: 2, email: "user2@example.com" },
  ];
} 