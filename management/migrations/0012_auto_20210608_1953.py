# Generated by Django 3.1.4 on 2021-06-08 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20210608_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='doctor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='payments',
            name='patient',
            field=models.CharField(max_length=200),
        ),
    ]
