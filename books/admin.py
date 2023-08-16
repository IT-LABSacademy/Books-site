from django.contrib import admin
from .models import CategoryModel, BookModel, AudioModel


admin.site.register(CategoryModel)
admin.site.register(BookModel)
admin.site.register(AudioModel)