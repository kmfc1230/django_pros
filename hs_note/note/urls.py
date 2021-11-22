from django.urls import path

from note import views

urlpatterns=[
    path('list',views.list_note),
]