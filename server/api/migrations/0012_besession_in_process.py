# Generated by Django 2.0.6 on 2018-06-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_besession_extracted_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='besession',
            name='in_process',
            field=models.BooleanField(default=False),
        ),
    ]
