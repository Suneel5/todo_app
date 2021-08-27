from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import todoform
from .models import task

# Create your views here.

def home(request):
    # titles =['learn this','learn that','dont waste times']
    taskes=task.objects.all()
    if request.method == 'POST':
        todo_form=todoform(request.POST)
        if todo_form.is_valid():
            #todo_form.save()
            return HttpResponse('todo added')
    else:
        todo_form=todoform()

    # form=todoform()
    #print(form)  

    context={'taskes': taskes,'form': todo_form}

    return render(request,'home.html',context)

