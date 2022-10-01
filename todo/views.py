from django.shortcuts import render,redirect 
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Todo
from django.views.generic.edit import UpdateView

from .forms import TodoAddForm

# Create your views here.
def homePage(request):
	if request.method == 'POST':
		form = TodoAddForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = TodoAddForm()

	todos = Todo.objects.filter(done=False)
	doned_todos = Todo.objects.filter(done=True)
	for todo in todos:
		if todo.priority == 'red':
			todo.priority = 'list-group-item-warning'
		elif todo.priority == 'green':
			todo.priority = 'list-group-item-success'
		elif todo.priority == 'yellow':
			todo.priority = 'list-group-item-info'
	context = {
		'todos':todos,
		'addform':form,
		'doned_todos':doned_todos
	}
	return render(request, 'index.html', context)

def doneTodo(request,todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.done = True
	todo.save()
	if todo:
		return redirect('todo:home')
	return render(request,'index.html')

def deleteTodo(request,todo_id):
	todo = Todo.objects.get(id=todo_id)
	todo.delete()
	return redirect('todo:home')

class UpdateTodoView(UpdateView):
	model = Todo
	fields = ['title', 'text','priority']
	template_name = 'update.html'
	success_url = '/'

