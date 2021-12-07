from django.urls import path

from note import views

urlpatterns = [
    path('list/', views.list_note),
    path('add/', views.add_note),
    path('del/<int:id>', views.del_note),
    path('update/<int:id>', views.update_note),
    path('restore/', views.restore),
]
