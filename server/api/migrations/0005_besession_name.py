# Generated by Django 2.0.6 on 2018-06-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180611_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='besession',
            name='name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]
