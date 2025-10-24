from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
  
urlpatterns = [
    # path("", views.base , name = "base"),
    path("", views.home , name = "home"),
    path("category/<slug:val>", views.CategoryView.as_view(),name="Category"),
    path("category-title/<slug:val>", views.CategoryTitle.as_view(),name="Category-title"),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name="product-detail"),
    
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)