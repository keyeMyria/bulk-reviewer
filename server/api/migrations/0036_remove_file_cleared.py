# Generated by Django 2.0.6 on 2018-07-19 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20180718_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='cleared',
        ),
    ]
