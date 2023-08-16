from django.db import models
from users.models import *


class CategoryModel(models.Model):
    icon = models.CharField(max_length=250)
    name = models.CharField(max_length=200, blank=False, null=True)
    
    def __str__(self):
        return self.name


class BookModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE, related_name='category')
    book_name = models.CharField(max_length=250)
    book_the_author = models.CharField(max_length=250)
    book_img = models.ImageField(upload_to='images/')
    book_genre = models.CharField(max_length=250)
    user = models.ForeignKey(UsersModel,on_delete=models.CASCADE, related_name='book_add_user')
    
    
    def __str__(self):
        return self.book_name
    
    
class AudioModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='audios')
    
    audio_file = models.FileField(upload_to='audios/')

    def __str__(self):
        return self.audio_file.name