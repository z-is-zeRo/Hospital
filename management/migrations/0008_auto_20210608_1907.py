# Generated by Django 3.1.4 on 2021-06-08 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_patients_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='age',
            new_name='phone',
        ),
    ]
