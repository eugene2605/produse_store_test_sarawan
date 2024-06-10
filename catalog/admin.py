from django.contrib import admin

from catalog.models import Category, Subcategory, Product, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'image',)
    list_filter = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category', 'image',)
    list_filter = ('name', 'category')
    search_fields = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'subcategory', 'image1', 'image2', 'image3', 'price')
    list_filter = ('name', 'subcategory')
    search_fields = ('name', 'subcategory')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'product', 'quantity',)
    list_filter = ('owner', 'product',)
    search_fields = ('owner', 'product',)
