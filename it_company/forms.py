
from django import forms
from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'you@company.com',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+972 50 000 0000',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about your project or IT needs...',
                'rows': 5,
            }),
        }
