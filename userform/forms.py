from django import forms
from .models import UserInfo

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'email', 'file']
