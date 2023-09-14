from django.contrib import admin

# Register your models here.
from .models import Category,Product

class Categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,Categoryadmin)

class Productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','available','stock']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 10
admin.site.register(Product,Productadmin)