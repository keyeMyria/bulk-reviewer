# Generated by Django 2.0.6 on 2018-06-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20180614_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='beconfig',
            name='regex_file',
            field=models.FileField(blank=True, null=True, upload_to='regex_files/'),
        ),
        migrations.AlterField(
            model_name='besession',
            name='annotated_feature_files_path',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='besession',
            name='dfxml_path',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='besession',
            name='extracted_transfer',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='besession',
            name='feature_files_path',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='context',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='feature',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='forensic_path',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feature',
            name='offset',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
