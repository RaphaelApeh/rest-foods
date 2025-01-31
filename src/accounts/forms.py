from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "w-full shadow-xs border border-gray-200 text-black p-2 block rounded-md mb-6 mt-2 focus:ring-red-800",
        "placeholder": "johndoe@example.com"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "w-full shadow-sm border border-gray-200 p-2 text-black rounded-md mb-2 mt-2 focus:ring-red-800",
        "placeholder": "********"
    }))