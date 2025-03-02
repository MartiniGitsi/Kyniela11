import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Tasks = () => {
    const [tasks, setTasks] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchTasks = async () => {
            try {
                const token = localStorage.getItem("token");
                if (!token) {
                    throw new Error("No authentication token found");
                }
        
                const response = await fetch("http://localhost:8000/tasks/tasks/", {
                    method: "GET",  //  Ensure it's a GET request
                    headers: {
                        "Authorization": `Bearer ${token}`,
                        "Content-Type": "application/json",
                    },
                });
        
                if (!response.ok) {
                    const errorText = await response.text();
                    throw new Error(`Error fetching tasks: ${errorText}`);
                }
        
                const data = await response.json();
                setTasks(data);
            } catch (error) {
                console.error("Failed to load tasks:", error);
            }
        };

        fetchTasks();
    }, [navigate]);

    return (
        <div className="p-6">
            <h2 className="text-2xl font-bold mb-4">Your Tasks</h2>
            <ul>
                {tasks.map((task) => (
                    <li key={task.id} className="p-2 border-b">{task.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default Tasks;