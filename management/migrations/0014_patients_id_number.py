# Generated by Django 3.1.4 on 2021-06-11 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0013_auto_20210608_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='id_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]