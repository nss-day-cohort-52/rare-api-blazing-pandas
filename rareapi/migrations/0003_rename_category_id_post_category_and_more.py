# Generated by Django 4.0.2 on 2022-02-16 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0002_category_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]
