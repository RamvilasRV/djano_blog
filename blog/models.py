from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	# image = models.ImageField() ## need to define a MEDIA_ROOT
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now=True)
	like_count = models.IntegerField(default=0) 
	category = models.CharField(max_length=50, null=True, blank=True)
	published = models.IntegerField(default=1)
	user= models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)


	### VALIDATION ###
	# Like_count should not be negative
	
	def __str__(self):
		return (self.title)


