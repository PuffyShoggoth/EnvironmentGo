from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Photo(models.Model):
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='photos')
