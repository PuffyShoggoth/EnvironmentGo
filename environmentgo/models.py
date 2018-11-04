from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    latitude = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/')
    invasive = models.BooleanField()
    description = models.CharField(max_length=500, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos')

