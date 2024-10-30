from django.shortcuts import render
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

def register(request):
    return render(request, 'core/register.html')

def settings(request):
    return render(request, 'core/settings.html')