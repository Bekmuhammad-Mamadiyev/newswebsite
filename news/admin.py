from django.contrib import admin

from .models import NewsModel,CategoryModel, Contacts

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name','id']

@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title','slug','publish_time','status']
    list_filter = ['publish_time','status']
    prepopulated_fields = {'slug':('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title','body']
    ordering = ['publish_time']

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject']
    search_fields = ['name','email','subject']