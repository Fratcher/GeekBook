from django.contrib import admin

# Register your models here.
from .models import Year, Description, Author

admin.site.register(Year)
admin.site.register(Description)
admin.site.register(Author)