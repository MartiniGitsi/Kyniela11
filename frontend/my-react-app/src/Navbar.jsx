import React from 'react';
import './styles/Navbar.css';
import { Link, useNavigate } from 'react-router-dom';

const Navbar = () => {
    const navigate = useNavigate();

    const handleLogout = () => {
        // Remove JWT token from localStorage
        localStorage.removeItem("token");

        // Redirect to the login page
        navigate("/login");
    };

    return (
        <nav className="navbar">
          <ul>
            <li>
              <Link to="/tasks">Tasks</Link>
            </li>
            <li>
              <Link to="/profile">Profile</Link>
            </li>
            <li>
              {/* If token exists, show logout button */}
              {localStorage.getItem('token') ? (
                <button onClick={handleLogout}>Logout</button>
              ) : (
                <Link to="/login">Login</Link> // Show login link if not logged in
              )}
            </li>
          </ul>
        </nav>
      );
    };

export default Navbar;