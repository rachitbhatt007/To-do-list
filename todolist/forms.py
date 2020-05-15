from django import forms
from todolist.models import todo

class taskform(forms.ModelForm):
	class Meta:
		model = todo
		fields = ('task','done') 