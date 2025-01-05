from django.contrib import admin
from .models import info
from froala_editor.fields import FroalaField

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_on"]
    content = FroalaField()