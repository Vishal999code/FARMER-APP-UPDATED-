# Generated by Django 3.2.9 on 2021-12-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='details',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='machine',
            name='fetures',
            field=models.TextField(),
        ),
    ]
