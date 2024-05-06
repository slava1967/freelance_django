from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя пользователя'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'}
        )
    )


class RegisterForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('freelancer', 'Фрилансер'),
        ('customer', 'Клиент'),
    ],
        widget=forms.RadioSelect(),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя пользователя'}
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Пароль'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Повторите пароль'}
        )
    )

    class Meta:
        model = User
        fields = ('role', 'username', 'email', 'password1', 'password2')
