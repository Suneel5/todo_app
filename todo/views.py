from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import todoform
from .models import task
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class taskCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')
    success_message = "New Task added" 
    def get(self, request, *args, **kwargs):       
        taskes=task.objects.filter(user_id=request.user.id) 
        context = {'form': todoform(),'taskes':taskes}
        return render(request, 'home.html', context)

    def post(self, request, *args, **kwargs):
        form = todoform(request.POST)

        if form.is_valid():
            # form.cleaned_data['user']=request.user.id
            # print(form.cleaned_data)
            post=form.save()
            post.user=request.user
            post.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        return render(request, 'home.html', {'form': form})
        
class taskUpdateView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):

    model = task
    fields = ['title','completed',]
    template_name='task_update.html'
    success_url=reverse_lazy('home')
    success_message='Task updated successfully!'


# class taskDeleteView(DeleteView):
#     model = task
#     success_url = reverse_lazy('home')

@login_required
def delete_task(request,pk):
    task.objects.get(id=pk).delete()
    return redirect('home')

