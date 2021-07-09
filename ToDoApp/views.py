from django.shortcuts import render
from django.http import HttpResponse
from . models import Tasks
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    model = Tasks.objects.all()
    return render(request, 'index.html', {
        "model" : model
    })


def tasks(request):
    if request.method == 'POST':
        tasks = Tasks(task = request.POST['task'])
        tasks.save()
        return render(request, 'tasks.html', {
            "message" : "Successfully Added !"
        })
    return render(request, 'tasks.html')


def delete(request, todo_id):
    fordel = Tasks.objects.get(id=todo_id)
    fordel.delete()        
    return HttpResponseRedirect(reverse('index'))
        


