from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post")
	title = models.CharField(max_length=300)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'Blog post {self.pk} by {self.author}'

