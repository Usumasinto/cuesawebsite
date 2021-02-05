from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
#from .models import user


def home(request):
    print(request.user)
    return render(request, 'home.html')




def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
# Create your views here.
