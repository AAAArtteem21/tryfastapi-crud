from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db

from services.task import TaskService


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    return TaskService(db)

