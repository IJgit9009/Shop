# Generated by Django 5.1.1 on 2024-09-09 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_userprofile_reviews_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
