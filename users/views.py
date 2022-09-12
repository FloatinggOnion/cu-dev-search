from http.client import ImproperConnectionState
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.core.mail import send_mail

# Create your views here.
def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # send_mail('Thanks for joining!', 'Thank you for joining CU Dev Search! You won\'t regret this decision!!!', 'noreply@cudevsearch.com', [form.cleaned_data['email']], fail_silently=False)

            return redirect('/')

    form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)