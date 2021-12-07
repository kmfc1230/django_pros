from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('book/list/', views.book_list),
    path('book/edit/', views.book_edit),
    path('book/add/', views.book_add),
    path('book/del/', views.book_del),
    path('author/list/', views.author_list),
    path('author/edit/', views.author_edit),
    path('author/add/', views.author_add),
    path('author/del/', views.author_del),
    path('pub/list/', views.pub_list),
    path('pub/edit/', views.pub_edit),
    path('pub/add/', views.pub_add),
    path('pub/del/', views.pub_del),

]
