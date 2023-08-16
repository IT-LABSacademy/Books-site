from django.urls import path
from .views import *


urlpatterns = [
    path("categories/<str:cate_id>/", categoriesView, name="categories"),
    path("my_books/<str:user_id>/", my_booksView, name="my_books"), 
    path("audios/<str:book_id>/", audiosView, name="audios"),
    path("search_results/", search_results, name="search_results"),
]
