from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import CustomUser

# Create your views here.
class UserProfileView(LoginRequiredMixin,  DetailView):
	model = CustomUser
	template_name = "users/user_profile.html"
	fields = ["name"]
	context_object_name = "CustomUser"
	