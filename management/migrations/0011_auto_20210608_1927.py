# Generated by Django 3.1.4 on 2021-06-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_patients_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='bloodpressure',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='haemoglobin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='heartbeat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='history',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='sugar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='timeline',
            field=models.TextField(blank=True, null=True),
        ),
    ]