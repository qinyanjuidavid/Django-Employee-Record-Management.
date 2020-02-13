from django import forms
from django.forms import ModelForm
from myapp.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['full_name','emp_code','education','mobile','position','cv','image','about']
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label='--Select--'
        self.fields['education'].empty_label="--Select--"
