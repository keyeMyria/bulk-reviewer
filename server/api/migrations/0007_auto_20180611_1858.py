# Generated by Django 2.0.6 on 2018-06-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_file_allocated'),
    ]

    operations = [
        migrations.AddField(
            model_name='besession',
            name='annotated_be_feature_files',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='besession',
            name='be_feature_files',
            field=models.TextField(blank=True, null=True),
        ),
    ]