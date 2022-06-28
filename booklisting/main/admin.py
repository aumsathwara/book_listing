from django.contrib import admin
from .models import Book_Item, Book_List

# Register your models here.

admin.site.register(Book_List)
admin.site.register(Book_Item)