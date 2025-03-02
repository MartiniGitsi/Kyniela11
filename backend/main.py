from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

# from database import SessionLocal
from database import get_db  # nuevo
from modelosdb import Task

from fastapi.middleware.cors import CORSMiddleware

from backend.routes import auth, tasks  # para personalizacion de usuarios

from fastapi.security import OAuth2PasswordBearer
from backend.auth import get_current_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

app = FastAPI(
    title="Your API Title",
    description="Description of the API",
    version="1.0.0",
)


# Add the Bearer JWT authentication security scheme to OpenAPI
@app.on_event("startup")
async def add_bearer_security():
    openapi_schema = app.openapi()

    # Add the Bearer JWT security scheme to OpenAPI components
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }

    # Assign this security scheme to all endpoints
    for path in openapi_schema["paths"].values():
        if isinstance(path, dict):
            for method in path.values():
                method["security"] = [{"bearerAuth": []}]

    # Update FastAPI app's OpenAPI schema with the modified one
    app.openapi_schema = openapi_schema


# Indicar que recibirá peticiones del origen del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the authentication router
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])


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
