from fastapi import APIRouter, Depends
from ..deps import get_current_user
from ..schemas.task import TaskCreate, TaskUpdate
from ..services.task_service import (
    list_tasks_for_user,
    create_task_for_user,
    update_task_for_user,
    delete_task_for_user,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("")
def list_tasks(current_user=Depends(get_current_user)):
    return list_tasks_for_user(current_user["id"])

@router.post("")
def create_task(payload: TaskCreate, current_user=Depends(get_current_user)):
    return create_task_for_user(current_user["id"], payload.title, payload.description)

@router.put("/{task_id}")
def update_task(task_id: int, payload: TaskUpdate, current_user=Depends(get_current_user)):
    return update_task_for_user(current_user["id"], task_id, payload.title, payload.description, payload.completed)

@router.delete("/{task_id}")
def delete_task(task_id: int, current_user=Depends(get_current_user)):
    return delete_task_for_user(current_user["id"], task_id)
