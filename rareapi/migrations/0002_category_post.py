# Generated by Django 4.0.2 on 2022-02-15 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('image_url', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('approved', models.BooleanField(default=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.category')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rareapi.rareuser')),
            ],
        ),
    ]