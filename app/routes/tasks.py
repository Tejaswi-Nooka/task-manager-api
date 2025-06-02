from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from .. import schemas, crud, models, database, auth

router = APIRouter(prefix="/tasks", tags=["Tasks"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> models.User:
    username = auth.decode_access_token(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.create_task(db, task, current_user.id)


@router.get("/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_tasks_by_user(db, current_user.id, skip=skip, limit=limit)


@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_task = crud.update_task(db, task_id, task, current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    return db_task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_task = crud.delete_task(db, task_id, current_user.id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found or unauthorized")
    return {"message": "Task deleted"}
