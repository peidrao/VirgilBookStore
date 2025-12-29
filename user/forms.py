from django.contrib.auth.forms import UserCreationForm

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
