from typing import Optional

from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from models.tasks import Task
from schemas.tasks import TaskIn


class TaskRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, data: TaskIn) -> Task:
        task = Task(**data.model_dump())
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_all(self) -> list[Task]:
        return self.db.query(Task).order_by(Task.id).all()

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.get(Task, task_id)

    def update(self, task: Task, data: dict) -> Task:
        for field, value in data.items():
            setattr(task, field, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()