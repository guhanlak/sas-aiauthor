import React from "react";
import LoginPage from "../components/LoginPage";
import { login } from "../services/api";
import { setToken } from "../utils/auth";

const Login = () => {
  const handleLogin = async ({ email, password, role }) => {
    const res = await login(email, password);
    setToken(res.access_token);
    alert("Logged in (placeholder)");
  };

  return <LoginPage onLogin={handleLogin} />;
};

export default Login; 