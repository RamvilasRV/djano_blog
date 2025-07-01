from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django import forms
from django.views import View
from django.urls import reverse_lazy


from .forms import CreateBlogForm ,CreateBlogModelForm
from .models import Blog
from users.models import CustomUser

## A view for showing all the te blogs from all users. Used function based view for this
def bloglist(request):
	blogs = Blog.objects.all().order_by('-created_time')
	context = {"blogs":blogs}
	return render(request, "blog/blogs.html", context)


## A view to show a single blog. Use Class based view for it..
class BlogDetailView(DetailView):
	def get(self, request, pk):
		try:
			blog = Blog.objects.get(pk=pk)
			context = {"blog":blog}
			return render(request, "blog/blogdetail.html",context)
		except:
			raise Http404()


## This view is reponsible to list all the blogs from a particular user
## Do you notice how there is no passing of context variable?? like the one above?
class UserBlogsView(LoginRequiredMixin, ListView):
	model = Blog
	template_name = 'blog/user_blogs.html'
	context_object_name = 'blogs'

	def get_queryset(self): ## do not pass variables as an argument to the function.
		username_slug = self.kwargs['username_slug'] ##self.kwargs contains the keywords captured from the url. (dictionary)
		user = CustomUser.objects.get(slug=username_slug)
		blogs = Blog.objects.filter(user=user).order_by('-created_time')
		return blogs



## below code was only done as an excersie. (function based views)
# @login_required
# def create_blog(request):
# 	if request.method=="POST":
# 		title = request.POST.get("title", "").strip()
# 		content = request.POST.get("content", "").strip()

# 		if title and content:
# 			Blog.objects.create(
# 				title = title,
# 				content = content,
# 				user = request.user
# 				)
# 			return redirect("/bloglist")
# 		else:
# 			error = "Title and content are required"
# 			return render(request, "blog/create_blog.html", {"error": error, "title": title, "content": content})

# 	return render(request, "blog/create_blog.html")


## This is also for an excersise (class based views)
# class CreateBlogView(View):
# 	def get(self, request):
# 		print("get")
# 		form = CreateBlogModelForm()
# 		return render(request, "blog/create_blog.html", {"form":form})

# 	def post(self, request):
# 		print("get")
# 		form = CreateBlogModelForm(request.POST)
# 		if form.is_valid():
# 			Blog.objects.create(
# 				title = form.cleaned_data['title'],
# 				content = form.cleaned_data['content'],
# 				user = request.user
# 				)
# 			return redirect("bloglist")
# 		else:
# 			return render(request, "blog/create_blog.html", {"form": form})


class CreateBlogView(LoginRequiredMixin, CreateView):
	model = Blog
	form_class = CreateBlogModelForm
	template_name = "blog/create_blog.html"
	
	def get_success_url(self):
		return reverse_lazy("bloglist")

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


class UpdateBlogView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "blog/update_blog.html"
    fields = ["title", "content"]
    success_url = reverse_lazy('bloglist')
