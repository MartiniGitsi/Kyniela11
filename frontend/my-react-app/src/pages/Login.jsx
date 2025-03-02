import { useState } from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    const handleLogin = async (e) => {
        e.preventDefault();
        setError(null);

        try {
            
            const formData = new URLSearchParams();
            formData.append("username", username);
            formData.append("password", password);
            
            const response = await fetch("http://localhost:8000/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: formData,  // Ensuring correct format
            });

            if (!response.ok) {
                //throw new Error("Invalid credentiales"+"|" + username + "|"+ password + "|" + ${errorText} );
                const errorText = await response.text();  // Read the actual error message
                throw new Error(`Invalid credentials | ${username} | ${password} | ${errorText}`);
            }

            const data = await response.json();
            localStorage.setItem("token", data.access_token);
            navigate("/tasks");  // Redirect to the task list
        } catch (err) {
            setError(err.message);
        }
    };

    return (
        <div className="flex items-center justify-center h-screen">
            <div className="p-6 bg-white rounded-lg shadow-lg">
                <h2 className="text-2xl font-bold mb-4">Login</h2>
                {error && <p className="text-red-500">{error}</p>}
                <form onSubmit={handleLogin}>
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="w-full p-2 mb-2 border rounded"
                        required
                    />
                    <input
                        type="password"
                        placeholder="Password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full p-2 mb-2 border rounded"
                        required
                    />
                    <button
                        type="submit"
                        className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
                    >
                        Login
                    </button>
                </form>
            </div>
        </div>
    );
};

export default Login;