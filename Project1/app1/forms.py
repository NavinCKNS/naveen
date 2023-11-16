from django import forms
from app1.models import student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=student
        fields="__all__"