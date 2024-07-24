from django import forms
from .models import Employee
from members.models import *

class EmployeeForm(forms.ModelForm):
    #this is an inner class within EmployeeForm that provide metadata for the form
    class Meta:
        #This specifies the specific model that will be associated with the form
        model=Employee
        #'all 'specifies the model fields from the Employee model
        fields="__all__"

class TrainerForm(forms.ModelForm):
    #this is an inner class within EmployeeForm that provide metadata for the form
    class Meta:
        #This specifies the specific model that will be associated with the form
        model=Trainer
        #'all 'specifies the model fields from the Employee model
        fields="__all__"

class PlayerForm(forms.ModelForm):
    #this is an inner class within EmployeeForm that provide metadata for the form
    class Meta:
        #This specifies the specific model that will be associated with the form
        model=Player
        #'all 'specifies the model fields from the Employee model
        fields="__all__"

class PaymentForm(forms.ModelForm):
    #this is an inner class within EmployeeForm that provide metadata for the form
    class Meta:
        #This specifies the specific model that will be associated with the form
        model=Payment
        #'all 'specifies the model fields from the Employee model
        fields="__all__"
class TrainingKitCollectionForm(forms.ModelForm):
    #this is an inner class within EmployeeForm that provide metadata for the form
    class Meta:
        #This specifies the specific model that will be associated with the form
        model=TrainingKitCollection
        #'all 'specifies the model fields from the Employee model
        fields="__all__"
        widgets = {
            'collection_date': forms.DateInput(attrs={'type': 'date'})
        }
