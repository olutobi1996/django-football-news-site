from django.db import models

class info(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    content = FroalaField()
def __str__(self):
        return self.name