from django.contrib import admin

from portal.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ['hidden']
    list_display = ('id', 'name', 'parent', 'hidden')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ['status']
    list_display = ('id', 'name', 'short_description', 'status')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
