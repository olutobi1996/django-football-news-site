from django.contrib import admin
from .models import Post
from froala_editor.fields import FroalaField


@admin.register(Post)
class PostAdmin(FroalaField.ModelAdmin):
    list_display = ["title","author","created_on"]
    list_display_links = ["title","created_on"]
    search_fields = ["title"]
    list_filter = ["created_on"]
    prepopulated_fields = {'slug':('title',)} 