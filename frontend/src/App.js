import "./App.css";
import React from "react";
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import MainPage from "./components/mainPage.js";
import Login from "./components/loginPage.js";
import Header from "./components/header.js";
import Test from "./components/test.js";

const isAuthenticated = true;
export default function App() {
  return (
    <div>
      <title>Sequoia Recruitment Tool</title>
      <body>
        <div className="container">
          <Header />
        </div>
        <BrowserRouter>
          <Routes>
            <Route path="login" element={<Login />} />
            {isAuthenticated ? (
              <Route path="/" element={<Test />} /> //What's actually calling the front end
            ) : (
              <Route path="/" element={<Navigate to="/login" />} />
            )}
          </Routes>
        </BrowserRouter>
      </body>
    </div>
  );
}
