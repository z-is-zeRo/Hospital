# Generated by Django 3.1.4 on 2021-06-08 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_auto_20210608_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='department',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='user',
        ),
    ]
