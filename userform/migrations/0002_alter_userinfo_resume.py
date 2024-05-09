# Generated by Django 4.2.13 on 2024-05-09 08:21

import django.core.validators
from django.db import migrations, models
import userform.validators


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='resume',
            field=models.FileField(upload_to='media', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['.docx', '.pdf', '.doc']), userform.validators.validate_file_size]),
        ),
    ]