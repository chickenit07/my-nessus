from django import forms
from mysite.core.models import Scan

class ScanningForm(forms.ModelForm):
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