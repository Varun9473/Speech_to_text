# Generated by Django 2.1 on 2019-04-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_fileupload_text_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='updated_url',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
