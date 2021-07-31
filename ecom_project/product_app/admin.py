from django.contrib import admin
from product_app.models import Categories,Products,Images

# Register your models here.
admin.site.register(Images)
admin.site.register(Categories)

class ProductsImagesInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductsAdmin(admin.ModelAdmin):
    list_display = [ 'title','status','created_at','updated_at','image_tag']
    list_filter = ['title','created_at']
    list_per_page = 10
    search_fields = ['title','new_price','details']
    inlines = [ProductsImagesInline]
    prepopulated_fields = {'slug': ('title','keywords')}




admin.site.register(Products,ProductsAdmin)
