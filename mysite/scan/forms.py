from django import forms
from .models import Scan

class ScanningForm(forms.ModelForm):
    # post = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Input Your Ip Address...',
    #         'label':'Ip Address'
    #     }
    # ))
    def __init__(self, *args, **kwargs):
        super(ScanningForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = Scan
        fields = ("__all__")