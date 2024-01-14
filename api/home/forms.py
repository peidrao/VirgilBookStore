from django import forms

from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:

        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        labels = {"name": "", "email": "", "subject": "", "message": ""}
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Seu nome",
                    "required": True,
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "email",
                    "placeholder": "Seu e-mail",
                    "required": True,
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "type": "text",
                    "placeholder": "Assunto",
                    "required": True,
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": "5",
                    "placeholder": "Sua mensagem",
                    "required": True,
                }
            ),
        }


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
