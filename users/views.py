from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # send_mail('Thanks for joining!', 'Thank you for joining CU Dev Search! You won\'t regret this decision!!!', 'noreply@cudevsearch.com', [form.cleaned_data['email']], fail_silently=False)

            return redirect('/login')

    form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)


def developers(request):
    users = User.objects.all()
    paginator = Paginator(users, 6)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'users': page_object,
    }
    
    return render(request, 'users/index.html', context)