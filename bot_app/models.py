from django.db import models

# Create my model
class Post(models.Model):
    name=models.CharField('user name',max_length=15)
    micropost=models.CharField('tweet',max_length=140,blank=True)

    def __str__(self):
        return self.name

class Picture(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)