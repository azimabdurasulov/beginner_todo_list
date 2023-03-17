from .models import Todo
from django.http import HttpRequest, JsonResponse

def get_all_task(request: HttpRequest)->JsonResponse:
    tasks = Todo.objects.all()
    result = []
    for task in tasks:
        result.append(task.to_dict())

    return JsonResponse({'result':result})

def get_task_id(request:HttpRequest, pk:int)->JsonResponse:
    try:
        # get product from database by id
        task = Todo.objects.get(id=pk)
        return JsonResponse(task.to_dict())
    except:
        return JsonResponse({"status": "object doesn't exist"})