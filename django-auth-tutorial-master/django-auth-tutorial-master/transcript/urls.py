
from django.urls import path, include
from . import views

urlpatterns = [
    path('transcript/<int:id>', views.transcript, name="transcript"),
    path('transcript/delete/<int:id>', views.deletefile, name="delete-transcript"),
    path('download/', views.Download, name="download"),
    path('update/',views.update, name="update"),
]