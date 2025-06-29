from django import forms

from .models import Blog

class CreateBlogForm(forms.Form):
	title = forms.CharField(max_length=120)
	content = forms.CharField(widget=forms.Textarea)

class CreateBlogModelForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = ["title", "content"]