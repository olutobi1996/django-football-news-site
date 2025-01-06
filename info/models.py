from django.db import models
from froala_editor.fields import FroalaField

class Info(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    content = FroalaField()
    def __str__(self):
        return self.name