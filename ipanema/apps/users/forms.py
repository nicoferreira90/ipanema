from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    """Form for creating new users with email as the primary identifier."""

    class Meta:
        model = get_user_model()
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """Form for updating users with email as the primary identifier."""

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name")
