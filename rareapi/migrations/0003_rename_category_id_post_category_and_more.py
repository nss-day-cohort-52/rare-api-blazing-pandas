
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
