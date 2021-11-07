from django.contrib import admin
from .models import Bd


# Register your models here.

class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'content', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd, BdAdmin)
