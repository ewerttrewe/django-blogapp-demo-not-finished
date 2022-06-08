from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='users_images')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)

		if img.height > 200 or img.width > 200:
			output_size = (150,150)
			img.thumbnail(output_size)
			img.save(self.image.path)