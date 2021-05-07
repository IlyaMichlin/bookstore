from django.contrib.auth import get_user_model  # derives from AUTH_USER_MODEL in settings.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    model = get_user_model()
    fields = ('email', 'username',)  # password field implicitly included


class CustomUserChangeForm(UserChangeForm):
    model = get_user_model()
    fields = ('email', 'username',)  # password field implicitly included
