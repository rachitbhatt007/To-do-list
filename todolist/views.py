from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse ,HttpResponseRedirect
from todolist.models import todo
from todolist.forms import taskform 
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
	if request.method=="POST":
		form =taskform(request.POST)
		if form.is_valid():
			print("inside valid")
			form=form.save(commit=False)
			form.owner = request.user
			form.save()
			messages.success(request,("New Task added to the list"))
		return redirect('todolist:Todolist')
	
			
	else:	
		taks = todo.objects.filter(owner=request.user)
		paginator = Paginator(taks , 5)
		page = request.GET.get('pg')
		taks = paginator.get_page(page)
		dic = {'list': taks}
		return render(request,'tdtemp.html',context=dic)

def contacts(request):
	return render(request,'contact.html',{})

def about(request):
	return render(request,'about.html',{})


def home(request):
	return render(request,'home.html',{})


def deletetask(request,task_id):
	task = todo.objects.filter(id=task_id)
	if(task.manage==request.user):
		task.delete()
		return redirect('todolist:Todolist')
	else:
		messages.error(request,("Access Restricted"))	


def updatetask(request,task_id):
	if request.method=="POST":
		taskobj = todo.objects.get(pk=task_id)
		form = taskform(request.POST,instance=taskobj)
		if form.is_valid():
			form.save()

			messages.success(request,("successfully updated"))
		return redirect('todolist:Todolist')
	else:	
		taskobj = todo.objects.get(pk=task_id)
		return render(request,'update.html',{'taskobj':taskobj})


def complete(request,task_id):

	task = todo.objects.get(id=task_id)
	if(task.manage==request.user):
		if(task.done==True):
			task.done=False
			task.save()
		else:
			task.done=True
			task.save()	
		return redirect('todolist:Todolist')
	else:
		messages.error(request,("Access Restricted"))	