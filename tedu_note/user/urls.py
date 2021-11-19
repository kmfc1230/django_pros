from django.urls import path

from user import views

urlpatterns = [
    path('index/', views.index),
    path('reg/', views.reg_view),
    path('login/', views.login_view),

]
