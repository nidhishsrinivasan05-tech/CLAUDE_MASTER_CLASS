from fastapi import HTTPException
from ..db.store import tasks

def list_tasks_for_user(user_id: int):
    return [task for task in tasks if task["owner_id"] == user_id]

def create_task_for_user(user_id: int, title: str, description: str):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "completed": False,
        "owner_id": user_id,
    }
    tasks.append(task)
    return task

def update_task_for_user(user_id: int, task_id: int, title: str, description: str, completed: bool):
    for task in tasks:
        if task["id"] == task_id and task["owner_id"] == user_id:
            task["title"] = title
            task["description"] = description
            task["completed"] = completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

def delete_task_for_user(user_id: int, task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id and task["owner_id"] == user_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Task not found")
