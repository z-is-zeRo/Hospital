# Generated by Django 3.1.4 on 2021-06-08 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20210608_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointments',
            old_name='age',
            new_name='phone',
        ),
    ]
