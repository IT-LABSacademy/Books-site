from django.urls import path
from .views import *

urlpatterns = [
    path('category_all/', CategoryView.as_view()),
    path('book_all/', BookView.as_view()),
    path('book_id/<int:pk>/', BookIDView.as_view()),

    # user
    path('user_create/', UserView.as_view()),

    path('by_category_id/<int:id>/', by_category_id),
]

