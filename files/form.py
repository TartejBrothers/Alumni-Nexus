from django import forms
from .models import Alumni
from django.forms import ModelForm, TextInput, EmailInput, NumberInput, CharField


class add_data(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ["name", "year", "degree", "email", "course"]
        common_style = "background: #d9d9d9; margin-bottom: 10px; border: none; font-size: 20px; color: white; opacity: 0.8; padding: 10px; color:#000000;width:100%;"
        labels = {
            "year": ("Graduation Year"),
        }

        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": f"{common_style}",
                    "placeholder": "Name",
                }
            ),
            "course": TextInput(
                attrs={
                    "class": "form-control",
                    "style": f"{common_style}",
                    "placeholder": "Ex. CSE",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": f"{common_style}",
                    "placeholder": "Email",
                }
            ),
            "year": NumberInput(
                attrs={
                    "class": "form-control",
                    "style": f"{common_style}",
                    "placeholder": "Year",
                }
            ),
            "degree": TextInput(
                attrs={
                    "class": "form-control",
                    "style": f"{common_style} R",
                    "placeholder": "B.Tech",
                },
            ),
        }

        for field in widgets:
            widgets[field].attrs["@media screen and (max-width: 700px)"] = {
                "style": {"width": "80%"}
            }
