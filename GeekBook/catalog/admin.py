from django.contrib import admin

# Register your models here.
from .models import Book, Month, Day, Image, Video

admin.site.register(Book)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Image)
admin.site.register(Video)