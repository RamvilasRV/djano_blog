from django.contrib import admin

from blog.models import Blog
from users.models import CustomUser

# Register your models here.
admin.site.register(Blog)
admin.site.register(CustomUser)
# admin.site.register(Comment)
