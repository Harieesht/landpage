from django.db import models
from django.core.validators import FileExtensionValidator
from .validators import validate_file_size


class UserInfo(models.Model):
    name=models.CharField(max_length=450)
    email=models.EmailField()
    resume=models.FileField(upload_to='media',validators=[
        FileExtensionValidator(allowed_extensions=['.docx','.pdf','.doc']),
        validate_file_size
    ])


    def __str__(self):
        return self.name
