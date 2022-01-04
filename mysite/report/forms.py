from django import forms
from mysite.core.models import Scan

class ReportForm(forms.ModelForm):

    class Meta:
        model = Scan
        fields = ("__all__")