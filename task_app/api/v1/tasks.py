from fastapi import APIRouter, Depends

from schemas import TaskIn, TaskOut, TaskUpdate
from services.tasks import TaskService

router = APIRouter(tags=["tasks"])


@router.post("/tasks", status_code=201, response_model=TaskOut)
def create_task(task: TaskIn, service: TaskService = Depends()):
    return service.create_task(task)


@router.get("/tasks", status_code=200, response_model=list[TaskOut])
def get_tasks(service: TaskService = Depends()):
    return service.get_tasks()


@router.get("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def get_task(task_id: int, service: TaskService = Depends()):
    return service.get_task(task_id)


@router.patch("/tasks/{task_id}", status_code=200, response_model=TaskOut)
def update_task(task_id: int, data: TaskUpdate, service: TaskService = Depends()):
    return service.update_task(task_id, data)


@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, service: TaskService = Depends()):
    service.delete_task(task_id)