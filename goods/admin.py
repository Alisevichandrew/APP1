from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# admin.site.register(Categories) - вместо этого запишем после '*'
# admin.site.register(Products)
# '*'


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    # передадим, какие поля будут запоняться автоматически
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    # передадим, какие поля будут запоняться автоматически
    prepopulated_fields = {"slug": ("name",)}
