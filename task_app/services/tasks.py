from fastapi import Depends, HTTPException

from models.tasks import Task
from repositories.tasks import TaskRepository
from schemas.tasks import TaskIn, TaskUpdate


class TaskService:
    def __init__(self, repository: TaskRepository = Depends()):
        self.repository = repository

    def create_task(self, data: TaskIn) -> Task:
        return self.repository.create(data)

    def get_tasks(self) -> list[Task]:
        return self.repository.get_all()

    def get_task(self, task_id: int) -> Task:
        task = self.repository.get_by_id(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found.")
        return task

    def update_task(self, task_id: int, data: TaskUpdate) -> Task:
        task = self.get_task(task_id)
        # exclude_unset - в БД попадут только поля, которые клиент реально прислал
        changes = data.model_dump(exclude_unset=True)
        return self.repository.update(task, changes)

    def delete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        self.repository.delete(task)