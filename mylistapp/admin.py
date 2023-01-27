from django.contrib import admin
from .models import MyList
# Register your models here.

@admin.register(MyList)
class ListAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'watched']
