# your_app/models.py
from django.db import models

class ImageData(models.Model):
    name = models.CharField(max_length=100)
    image_base64 = models.TextField()

    def __str__(self):
        return self.name