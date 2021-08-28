from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import todoform
from .models import task
# Create your views here.

def home(request):
    taskes=task.objects.all()
    if request.method == 'POST':
        todo_form=todoform(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return redirect('home')
    else:
        todo_form=todoform()



    context={'taskes': taskes,'form': todo_form}

    return render(request,'home.html',context)

