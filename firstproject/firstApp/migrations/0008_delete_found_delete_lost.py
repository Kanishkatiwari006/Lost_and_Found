# Generated by Django 4.1 on 2024-01-29 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0007_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='found',
        ),
        migrations.DeleteModel(
            name='lost',
        ),
    ]
