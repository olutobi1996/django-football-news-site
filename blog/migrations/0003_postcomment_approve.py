# Generated by Django 4.2.17 on 2025-01-15 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]