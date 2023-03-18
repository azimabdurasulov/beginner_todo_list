from .models import Todo
from django.http import HttpRequest, JsonResponse
import json

def get_all_task(request: HttpRequest)->JsonResponse:
    if request.method == 'GET':
        tasks = Todo.objects.all()
        result = []
        for task in tasks:
            result.append(task.to_dict())

        return JsonResponse({'result':result})
    elif request.method == 'POST':
        decoded = request.body.decode()
        todos = json.loads(decoded)
        task = todos.get('task',False)
        description = todos.get('description', False)
        completed = todos.get('completed', False)
        created_at = todos.get('created_at',False)
        updated_at = todos.get('updated_at', False)

        if task:
            return JsonResponse({'status': 'task field is required'})
        if description:
            return JsonResponse({"status": 'description field is required'})
        
        tasks = Todo(
            task=task,
            description=description,
            completed=completed,
            created_at=created_at,
            updated_at=updated_at
        )

        tasks.save()
        return JsonResponse(tasks.to_dict())

def get_task_id(request:HttpRequest, pk:int)->JsonResponse:
    if request.method == 'GET':
        try:
            # get task from database by id
            task = Todo.objects.get(id=pk)
            return JsonResponse(task.to_dict())
        except:
            return JsonResponse({"status": "object doesn't exist"})
        
    if request.method == 'POST':
        decoded = request.body.decode()
        tasks = json.loads(decoded)
        task = tasks.get('task',False)
        description = tasks.get('description',False)
        completed = tasks.get('completed',False)
        created_at = tasks.get('created_at',False)
        updated_at = tasks.get('updated_at',False)

        todos = Todo.objects.get(id=pk)
        if task:
            todos.task=task
        if description:
            todos.description=description
        if completed:
            todos.completed=completed
        if created_at:
            todos.created_at=created_at
        if updated_at:
            todos.updated_at=updated_at

        todos.save()
    return JsonResponse(todos.to_dict())