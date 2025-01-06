from django.contrib import admin
from .models import Info
from froala_editor.fields import FroalaField

@admin.register(Info)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title","slug"]
    