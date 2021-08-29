from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import todoform
from .models import task
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy,reverse

# Create your views here.
class taskCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        taskes=task.objects.all()  
        context = {'form': todoform(),'taskes':taskes}
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            # book.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'home.html', {'form': form})
class taskUpdateView(UpdateView):
    model = task
    fields = ['title','completed']

class taskDeleteView(DeleteView):
    model = task
    success_url = reverse_lazy('home')
