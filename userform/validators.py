from django.core.exceptions import ValidationError


def validate_file_size(value):
    limit=20*1024*1024
    if value.size > limit:
        raise ValidationError("File size cannot exceed 20 mb")
    