from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#from .models import user


class profile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'