# Generated by Django 2.0.6 on 2018-06-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180628_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='forensic_path',
            field=models.TextField(blank=True),
        ),
    ]
