# Generated by Django 4.1 on 2024-01-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_found'),
    ]

    operations = [
        migrations.AlterField(
            model_name='found',
            name='Num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lost',
            name='Num',
            field=models.IntegerField(),
        ),
    ]
