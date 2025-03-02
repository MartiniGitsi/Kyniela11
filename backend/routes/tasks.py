from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from modelosdb import Task
from backend.auth import get_current_user

router = APIRouter()


@router.get("/tasks/")
def get_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Fetch only tasks belonging to the authenticated user"""
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks


@router.post("/tasks/")
def create_task(
    title: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    """Create a new task for the authenticated user"""
    new_task = Task(title=title, user_id=current_user.id)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
