from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, UserManager

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address",
                "required": "True"
            }
        )
    )

    last_name = forms.CharField(
        label="Last Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Last Name",
                "required": "True"
            }
        )
    )

    first_name = forms.CharField(
        label="First Name",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First Name",
                "required": "True"
            }
        )
    )

    nickname = forms.CharField(
        label="Nickname",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nickname",
                "required": "True"
            }
        )
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "required": "True"
            }
        )
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password Confirmation",
                "required": "True"
            }
        )
    )

    class Meta:
        model = User
        fields = ("email", "last_name", "first_name", "nickname")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data["email"])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password"
    )

    class Meta:
        model = User
        fields = ("email", "password", "last_name", "first_name", "is_active",)

    def clean_password(self):
        return self.initial["password"]