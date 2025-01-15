from django.contrib import admin
from .models import Post
from .models import PostComment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_on"]
    list_display_links = ["title","created_on"]
    search_fields = ["title"]
    list_filter = ["created_on"]
    prepopulated_fields = {'slug':('title',)} 

admin.site.register(PostComment)