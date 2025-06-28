from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404




from .models import Blog
from users.models import CustomUser

## A view for showing all the te blogs from all users. Used function based view for this
def bloglist(request):
	blogs = Blog.objects.all().order_by('created_time')
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
## Do you notice how there is no passing of context?? like the one above?
class UserBlogsView(LoginRequiredMixin, ListView):
	model = Blog
	template_name = 'blog/user_blogs.html'
	context_object_name = 'blogs'

	def get_queryset(self):
		username_slug = self.kwargs['username_slug']
		user = CustomUser.objects.get(slug=username_slug)
		blogs = Blog.objects.filter(user=user).order_by('-created_time')
		return blogs

