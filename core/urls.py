"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import get_all_task, get_task_id, delete_task_id, completed_task, incompleted_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', get_all_task),
    path('api/tasks/<int:pk>', get_task_id),
    path('api/tasks/<int:pk>/delete/', delete_task_id),
    path('api/tasks/completed/', completed_task),
    path('api/tasks/incompleted/', incompleted_task)
]