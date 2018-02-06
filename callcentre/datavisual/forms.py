from django import forms
from .models import CallRecord

class ImportExcelForm(forms.Form):
    file  = forms.FileField(label= "Choose excel to upload") 