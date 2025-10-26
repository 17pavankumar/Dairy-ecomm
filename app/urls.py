from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
    # path("", views.base , name = "base"),
    path("", views.home , name = "home"),
    path("about/", views.about , name = "about"),
    path("contact/", views.contact , name = "contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="Category"),
    path("category-title/<slug:val>", views.CategoryTitle.as_view(),name="Category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    
    #login authentication
    path("registration/", views.CustomerRegistrationView.as_view() , name='customerregistration'),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)