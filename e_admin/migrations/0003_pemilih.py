# Generated by Django 3.0.8 on 2020-09-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_admin', '0002_auto_20200902_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pemilih',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=6, unique=True)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('batas', models.PositiveSmallIntegerField()),
            ],
            options={
                'verbose_name': 'Pemilih',
                'verbose_name_plural': 'Pemilihs',
            },
        ),
    ]
