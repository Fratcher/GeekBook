from django.contrib import admin

# Register your models here.
from .models import Book, Month, Day, Image, Video

#admin.site.register(Book)
admin.site.register(Month)
#admin.site.register(Day)
#admin.site.register(Image)
#admin.site.register(Video)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('date',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'user', 'day', 'desc')
    list_filter = ('image', str('user'), 'day', 'desc',)
    fieldsets = (  
        (None, {
            'fields': ('day', 'user',)
        }),
        ('Image and Description', {
            'fields': ('image', 'desc')
        }),
    )

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'user', 'day', 'desc',)
    #changing the layout for new video
    fieldsets = (  
        (None, {
            'fields': ('day', 'user',)
        }),
        ('Video and Description', {
            'fields': ('video', 'desc')
        }),
    )