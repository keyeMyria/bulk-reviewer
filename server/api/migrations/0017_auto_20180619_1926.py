# Generated by Django 2.0.6 on 2018-06-19 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20180619_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='file_type',
            new_name='mime_type',
        ),
    ]