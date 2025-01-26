from django.contrib import admin
from .models import Post, PostComment

# Post register admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

# Post Comment register admin
@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'post', 'created_on', 'approve')
    list_filter = ('approve', 'created_on')
    search_fields = ('comment', 'user__username', 'post__title')