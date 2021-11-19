from django.urls import path

from mynote import views

urlpatterns = [
    path('list_note/', views.list_note),
    path('add/', views.add_note),
    path('update/<int:note_id>', views.update_note),
    path('delete/<int:note_id>', views.delete_note),
    path('restore/', views.restore),
]
