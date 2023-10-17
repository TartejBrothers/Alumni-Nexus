from django import forms
from .models import Alumni
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ["name", "year", "degree", "email", "course"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000",
                    "placeholder": "Name",
                }
            ),
            "course": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000",
                    "placeholder": "Ex. CSE",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000",
                    "placeholder": "Email",
                }
            ),
            "year": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000",
                    "placeholder": "Year",
                }
            ),
            "degree": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px; background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000",
                    "placeholder": "Ex. B.Tech",
                }
            ),
        }
