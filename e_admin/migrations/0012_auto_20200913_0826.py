# Generated by Django 3.0.8 on 2020-09-13 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_admin', '0011_voting_pilihanumum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pemilih',
            name='batas',
        ),
        migrations.AddField(
            model_name='voting',
            name='batas',
            field=models.PositiveSmallIntegerField(default='1'),
            preserve_default=False,
        ),
    ]
