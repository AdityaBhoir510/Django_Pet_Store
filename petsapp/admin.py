from django.contrib import admin
from .models import Pet

# Register your models here.
@admin.register(Pet)
class petAdmin(admin.ModelAdmin):
    list_display=("id","name","age","gender","breed","price") 

# admin.site.register(pet)