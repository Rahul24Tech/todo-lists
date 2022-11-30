from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success':False}
    if request.method == "POST":
        task = request.POST['title']
        desc = request.POST['desc']
        instance = Task(taskTitle=task, taskDesc=desc)
        instance.save()
        context = {'success':True}
    return render(request, "index.html", context)


def task(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, "task.html", context)