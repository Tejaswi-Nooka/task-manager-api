from sqlalchemy.orm import Session
from . import models, schemas
from .auth import hash_password


# ------------- User CRUD -------------

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_pw = hash_password(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# ------------- Task CRUD -------------

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).offset(skip).limit(limit).all()


def get_task(db: Session, task_id: int, user_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == user_id).first()


def update_task(db: Session, task_id: int, task: schemas.TaskCreate, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db.commit()
        db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int, user_id: int):
    db_task = get_task(db, task_id, user_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
