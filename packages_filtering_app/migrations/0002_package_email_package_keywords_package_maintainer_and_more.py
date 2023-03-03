# Generated by Django 4.1.7 on 2023-03-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages_filtering_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='package',
            name='keywords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='package',
            name='maintainer',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='package',
            name='version',
            field=models.TextField(default=''),
        ),
    ]