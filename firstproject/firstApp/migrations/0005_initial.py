# Generated by Django 4.1 on 2024-01-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('firstApp', '0004_delete_found_delete_lost'),
    ]

    operations = [
        migrations.CreateModel(
            name='found',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Product', models.CharField(max_length=50)),
                ('Other', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=1000)),
                ('Pin', models.IntegerField()),
                ('Num', models.IntegerField()),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='lost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Product', models.CharField(max_length=50)),
                ('Other', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=1000)),
                ('Pin', models.IntegerField()),
                ('Info', models.CharField(max_length=500)),
                ('Num', models.IntegerField()),
                ('Image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]