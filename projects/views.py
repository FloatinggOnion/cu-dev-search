from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project
from .forms import ProjectForm
from django.core.paginator import Paginator

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    print('PROJECT:', projects)

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'projects': page_object,
    }
    return render(request, 'projects/projects.html', context) 


def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    tags = projectObject.tags.all() #The tags associated with the project
    reviews = projectObject.reviews.all()

    context = {
        'project':projectObject,
        'tags':tags,
        'reviews':reviews
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):

    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

        return redirect('projects')

    form = ProjectForm()

    context = {
        'form':form,
    }
    return render(request, 'projects/project-form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()

        return redirect('projects')

    context = {
        'form':form,
    }
    return render(request, 'projects/project-form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()

        return redirect('projects')

    context = {
        'object':project,
    }

    return render(request, 'projects/delete.html', context)