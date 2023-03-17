from .models import Todo
from django.http import HttpRequest, JsonResponse

def get_all_task(request: HttpRequest)->JsonResponse:
    tasks = Todo.objects.all()
    result = []
    for task in tasks:
        result.append(task.to_dict())

    return JsonResponse({'result':result})