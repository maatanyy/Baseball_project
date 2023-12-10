from django.contrib import admin
from . models import *
# Register your models here.

admin.site.register(Comment)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body']
    list_display_links = ['id', 'title']
    ordering= ['title']
    list_filter = ['tag']
    search_fields = ['body']
    list_per_page = 5
    
    fieldsets = (
        ('기본정보', {'fields':('title','body')}),
        ('기타정보', {'fields':('tag', 'ip')})
    )

admin.site.register(Post, PostAdmin)