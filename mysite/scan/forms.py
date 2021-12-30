from django import forms
from .models import Scan

class ScanningForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Input Your Ip Address...',
            'label':'Ip Address'
        }
    ))

    class Meta:
        model = Scan
        fields = ("__all__")
