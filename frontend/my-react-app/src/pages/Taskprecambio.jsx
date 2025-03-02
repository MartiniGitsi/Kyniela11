import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Tasks = () => {
    const [tasks, setTasks] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchTasks = async () => {
            const token = localStorage.getItem("token");
            const response = await fetch("http://localhost:8000/tasks/", {
            //const response = await fetch("http://localhost:8000/tasks/tasks/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setTasks(data);
            } else {
                navigate("/login"); // Redirect to login if unauthorized
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