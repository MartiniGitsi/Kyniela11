from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlalchemy.orm import Session
from datetime import timedelta

from database import get_db
from modelosdb import User
from backend.auth import get_password_hash, verify_password, create_access_token
from pydantic import BaseModel

router = APIRouter()


# Define Pydantic models for request validation
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


# Register endpoint - does not require authentication
@router.post("/register/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    hashed_password = get_password_hash(user.password)
    new_user = User(
        username=user.username, email=user.email, hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


"""
@router.post("/login/")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=timedelta(minutes=30)
    )

    return {"access_token": access_token, "token_type": "bearer"}
"""


@router.post("/login/")
def login(
    username: str = Form(...),  # Make sure it uses Form
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
