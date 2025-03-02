import { useState, useEffect } from "react";


import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./Navbar";  // Import the Navbar component
import Login from "./pages/Login";
import Tasks from "./pages/Tasks";


const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000/tasks";


const PrivateRoute = ({ element }) => {
  const token = localStorage.getItem("token");
  return token ? element : <Navigate to="/login" />;
};


function App() {
  return (
      <Router>      
          <Navbar />  {/* Add Navbar to your layout */}
          <div style={{ padding: '20px' }}>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/tasks" element={<Tasks />} />
                <Route path="*" element={<Login />} />
            </Routes>  
          </div>      
      </Router>
  );
}



export default App;