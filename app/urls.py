from django.urls import path
from app import views


urlpatterns = [
    # path("", views.base , name = "base"),
    path("", views.home , name = "home"),
    
]
