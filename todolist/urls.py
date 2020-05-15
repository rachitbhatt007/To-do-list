from django.urls import path
from todolist import views

app_name = 'todolist'

urlpatterns = [
	path('', views.todolist , name='Todolist'),
	path('delete/<task_id>', views.deletetask , name='delete'),
	path('update/<task_id>', views.updatetask , name='update'),
	path('complete/<task_id>', views.complete , name='complete'),
	
]