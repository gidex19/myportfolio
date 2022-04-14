
from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Your Fullname', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    email_address = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email Address', 'class': 'form-control mb-3 inputfield', 'id': 'inputemail'}),
        required=False,
        label="")
