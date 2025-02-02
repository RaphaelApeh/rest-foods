from django import forms
from django.utils.crypto import get_random_string
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


CSS_CLASS = "w-full shadow-xs border border-gray-200 text-black p-2 block rounded-md mb-6 mt-2 focus:ring-red-800"

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": CSS_CLASS,
        "placeholder": "johndoe@example.com"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": CSS_CLASS,
        "placeholder": "********"
    }))


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email", 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({ "class": CSS_CLASS})
            self.fields[field].required = True

    def save(self, commit=True):
        instance =  super().save(commit=False)
        instance.username = get_random_string(10)
        
        if commit:
            return instance.save()
        return instance
    
    def clean_password(self):
        password = self.cleaned_data['password']
        try:
            validate_password(password)
        except Exception as e:
            raise forms.ValidationError(" ".join(e))
        return password

    def clean_email(self):
        email = self.cleaned_data["email"]
        if email is None or User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Invalid email or Email already exists.")
        
        return email
    
class EmailVerificationForm(forms.Form):

    verification_code = forms.CharField(widget=forms.TextInput(attrs={
        "class": CSS_CLASS,
        "placeholder": "Verification Code",
        "id": "form-input"
    }))