from django import forms

class ScanningForm(forms.Form):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'IP Address...',
        }
    ))