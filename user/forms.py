from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class LoginAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, profile):
        if not profile.is_active:
            raise forms.ValidationError("This account is inactive")
        if profile.username.startswith("b"):
            raise forms.ValidationError(
                "Sorry, accounts starting with 'b' aren't welcome here."
            )


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label="Nome de usuário",
        max_length=120,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Nome de usuário",
            }
        ),
    )
    password = forms.CharField(
        label="Senha",
        max_length=120,
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "form-control form-control-sm", "placeholder": "Senha"}
        ),
    )

    class Meta:
        model = Profile
        fields = ("username", "password")
