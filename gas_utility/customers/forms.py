# forms.py
from django import forms
from .models import User,ServiceRequest
from django.contrib.auth import authenticate

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'confirm_password', 'is_representative']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

    
    
class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_subject', 'description', 'attachment']  

    def __init__(self, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields['attachment'].required = False  