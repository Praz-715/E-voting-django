# Generated by Django 3.0.8 on 2020-09-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kandidat',
            name='suara',
            field=models.PositiveIntegerField(default=0),
        ),
    ]