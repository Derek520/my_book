from django.contrib import admin

# Register your models here.
from .models import BookInfo

admin.site.register(BookInfo)