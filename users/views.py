from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreation


# Create your views here.
class CreateUser(CreateView):
    form_class = CustomUserCreation
    template_name = 'users/signup.html'
    def get_success_url(self):
        return reverse('home')

