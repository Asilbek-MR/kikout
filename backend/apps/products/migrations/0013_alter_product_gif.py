# Generated by Django 4.2.8 on 2024-01-24 11:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_banner_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gif',
            field=models.FileField(null=True, upload_to='product/gif/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'mov'])]),
        ),
    ]