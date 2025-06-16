from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Blog

def blogs(request):
	blogs = Blog.objects.all().order_by('created_time')
	context = {"blogs":blogs}
	return render(request, "blogs.html", context)