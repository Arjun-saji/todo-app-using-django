from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 

# Create your views here.
def index(request):
	tasks=Task.objects.all()
	context={"tasks":tasks}
	return render(request,"todoapp/index.html",context)

def addtask(request):
	if request.method=="POST":
		title=request.POST.get("title")
		if title:
			Task.objects.create(title=title)
			return redirect('index')
	return render(request,"todoapp/add.html")


def edittask(request,task_id):
	task=Task.objects.get(pk=task_id)
	#task = get_object_or_404(Task, pk=task_id)
	if request.method=="POST":
		new=request.POST.get('title')
		if new:
			task.title= new
			task.save()
			return redirect('index')

	return render(request,"todoapp/edit.html",{"task":task})

def deletetask(request,task_id):
	task=Task.objects.get(pk=task_id)
	if request.method=="POST":
		task.delete()
		return redirect('index')
	return render(request,"todoapp/delete.html",{"task":task})



