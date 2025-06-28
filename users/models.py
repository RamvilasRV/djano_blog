from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class CustomUserManager(UserManager):
	"""This is a custom manager for the user class that we are going to make"""
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError("Please enter a valid email")
		if not password:
			raise ValueError("Please set a password")

		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_user(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", False)
		extra_fields.setdefault("is_superuser", False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email=None, password=None, **extra_fields):
		extra_fields.setdefault("is_staff", True)
		extra_fields.setdefault("is_superuser", True)
		return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
	"""A custom model for the User"""
	email = models.EmailField(blank=True, default="", unique=True)
	name = models.CharField(max_length=255, blank=True, default="")
	slug = models.SlugField(unique=True, blank=True)

	is_active=models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(blank=True, null=True)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email' 
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

	"""implementing the functions that django comes with."""
	def get_full_name(self):
		return self.name

	def get_short_name(self):
		return self.name or self.email.split("@")[0]

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super().save(*args, **kwargs)




"""
Why is there no password=password when creating a user model at line 15
 - Because you should never assign the raw password directly to the user model. Django needs to hash the password using a secure algorithm like PBKDF2 or Argon2

Why is there no password field in the model?
	- Password field is inherited from the AbstractBaseUser.
	- It comes with password and last_login fields and set_password(), check_password(), get_session_auth_hash()	

Is it really necessary to set the values for is_superuser and is_staff in the models? since it is already there in the manager?
	- Not strictly necessary, but is a good practice.
"""