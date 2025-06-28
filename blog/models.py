from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	# image = models.ImageField() ## need to define a MEDIA_ROOT
	created_time = models.DateTimeField(auto_now_add=True)
	updated_time = models.DateTimeField(auto_now=True)
	# like_count = models.IntegerField(default=0) 
	category = models.CharField(max_length=50, null=True, blank=True)
	published = models.IntegerField(default=1)
	slug = models.SlugField(unique=True, blank=True)
	user= models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
	# count_of_comments -> will have to calculate on the go.


	### VALIDATION ###
	# Like_count should not be negative
	
	def __str__(self):
		return (self.title)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)




# class Comment(models.Model):
# 	comment = models.TextField()
# 	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
# 	user= models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

# 	def __str__(self):
# 		return (self.comment[0:10]+".... by "+self.user.name)