from django.contrib import admin
from app.models import Product
# Register your models here.

admin.site.register(Product)
class productModelAdmin (admin.ModelAdmin):
    list_display = ['id', 'title','discounted_price', 'category','product_image']