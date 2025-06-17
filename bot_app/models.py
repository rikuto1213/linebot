from django.db import models

# Create my model　
#データベースと関連するフィールドを定義する
class Picture(models.Model):
    food_pic=models.ImageField(upload_to='images/')
    food_name=models.CharField("title",max_length=200)

    def __str__(self):
        return self.title

class Post(models.Model):
    name=models.CharField('user name',max_length=15)
    micropost=models.CharField('tweet',max_length=140,blank=True)

    def __str__(self):
        return self.name

    

