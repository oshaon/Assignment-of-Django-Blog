from django.contrib import admin
from .models import *

#show slug and category on admin dashboard
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category','status')
    list_filter = ('category','status',)

# Register your models here.
admin.site.register(Blog_info)
admin.site.register(Blog_section)
admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Author)

