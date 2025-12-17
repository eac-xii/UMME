from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email address",
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
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password confirmation",
                "required": "True"
            }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "last_name", "first_name", "nickname")
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        User = get_user_model()
        user = User.objects.create_user(
            email=self.cleaned_data["email"],
            last_name=self.cleaned_data["last_name"],
            first_name=self.cleaned_data["first_name"],
            nickname=self.cleaned_data["nickname"],
            password=self.cleaned_data["password1"]
        )

        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="Password"
    )

    class Meta:
        model = get_user_model()
        fields = ("email", "password", "last_name", "first_name", "is_active",)

    def clean_password(self):
        return self.initial["password"]