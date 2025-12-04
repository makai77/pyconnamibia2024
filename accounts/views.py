from django.shortcuts import render

from django.contrib.auth.views import LoginView
from .forms import PasskeyLoginForm

class CustomLoginView(LoginView):
    form_class = PasskeyLoginForm
    template_name = 'account/login.html' 
    
    

