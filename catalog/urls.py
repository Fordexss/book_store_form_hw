from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('add_book/', views.add_book, name='add_book'),
]
