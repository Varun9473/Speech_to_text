from django.urls import path

from . import views
from .views import Fileupload

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/', Fileupload),
]
