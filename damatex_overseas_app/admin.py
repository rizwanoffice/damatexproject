from django.contrib import admin
from .models import Category, Product, ProductImages, CarousalImages

# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImages
    #raw_id_fields = ['product']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
admin.site.register(Product, ProductAdmin)


# admin.site.register(ProductImages)
admin.site.register(CarousalImages)
