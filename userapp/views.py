from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from userapp.forms import customform
# Create your views here.
def register(request):
	if request.method=="POST":
		form = customform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,("Account created"))
			return redirect('userapp:register')
		

			
	register_form = customform()
	return render(request,'register.html',{'register_form':register_form})
