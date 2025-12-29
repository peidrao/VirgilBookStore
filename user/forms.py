from django.contrib.auth.forms import UserCreationForm

from user.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = (
            "email",
            "password1",
            "password2",
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        full_name = self.data.get("name", "").strip()
        parts = full_name.split(" ", 1)

        user.first_name = parts[0]
        user.last_name = parts[1] if len(parts) > 1 else ""

        if commit:
            user.save()

        return user
