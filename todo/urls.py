from django.urls import path
from . import views

urlpatterns = [
    path('',views.taskCreateView.as_view(),name='home')
    
]