from django.contrib import admin
# We need import all models from the "app" using .models
from .models import Product


# Register your models here.

# admin.site.register(Product)
# admin.register(Product) is for declaring we will use Product Model
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    # This line is for display the other attributes in the Model Product
    list_display = ('name', 'category', 'description', 'price')
    # This is for "make" a filter by Categories
    list_filter = ('category',)
