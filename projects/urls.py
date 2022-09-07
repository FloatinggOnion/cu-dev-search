from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('create/', views.createProject, name='create-project'),
    path('update/<str:pk>/', views.updateProject, name='update-project'),
    path('delete/<str:pk>/', views.deleteProject, name='delete-project'),
]