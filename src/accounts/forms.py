from django import forms
from django.utils.crypto import get_random_string
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "w-full shadow-xs border border-gray-200 text-black p-2 block rounded-md mb-6 mt-2 focus:ring-red-800",
        "placeholder": "johndoe@example.com"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full shadow-sm border border-gray-200 p-2 text-black rounded-md mb-2 mt-2 focus:ring-red-800",
        "placeholder": "********"
    }))


class RegisterForm(forms.Form):
    
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={
            'class': "w-full shadow-sm border border-gray-200 p-2 text-black rounded-md mb-2 mt-2 focus:ring-red-800",
            'placeholder': 'Email'
            })) 

    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
            'class': "w-full shadow-sm border border-gray-200 p-2 text-black rounded-md mb-2 mt-2 focus:ring-red-800",
            'placeholder': 'Password'
            })) 
    
    
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
    
    def save(self):
        username = get_random_string(10)
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = User.objects.create_user(username=username, email=email, password=password)

        return user