from django.urls import path
from . import views

urlpatterns = [
    path('',views.taskCreateView.as_view(),name='home'),
    path('update/<int:pk>',views.taskUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.delete_task,name='delete')
    
]