# Generated by Django 3.1.4 on 2021-06-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_auto_20210608_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]