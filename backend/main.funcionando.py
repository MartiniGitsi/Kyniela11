from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# from database import SessionLocal
from database import get_db  # nuevo
from modelosdb import Task

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Indicar que recibirá peticiones del origen del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic model to validate request data
class TaskCreate(BaseModel):
    title: str


# Get all tasks
@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):  # Dependency Injection
    return db.query(Task).all()


# Create a new task
@app.post("/tasks")
def create_task(
    task: TaskCreate, db: Session = Depends(get_db)
):  # Dependency Injection
    new_task = Task(title=task.title)  # Access the `title` field correctly
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Mark task as completed
@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.completed = True
    db.commit()
    db.refresh(task)
    return task


# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
