# Generated by Django 5.0.3 on 2024-03-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_login',
            field=models.BooleanField(default=False),
        ),
    ]
