from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_variables
from django.shortcuts import (
    render,
    redirect
)
from django.views.generic import (
    FormView,
    View
    )
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model
)

from .forms import (
    LoginForm,
    RegisterForm
)
from .decorators import redirect_login_user


User = get_user_model()

@method_decorator(redirect_login_user, name="dispatch")
@method_decorator(sensitive_variables("email", "password"), name="form_valid")
class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    success_url = "/"

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Successfully Logged in.")
            return super().form_valid(form)
        messages.error(self.request, "No user with this email and password.")
        return self.form_invalid(form)
    

@method_decorator(login_required, name="dispatch")
class LogoutView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "accounts/logout.html")
    
    
    def post(self, request, *args, **kwargs):
        
        logout(request)
        return redirect("login")
    
@method_decorator(redirect_login_user, name="dispatch")
class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = RegisterForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Account created successfully!")
            return super().form_valid(form)
        messages.error(self.request, 'Something went wrong.')
        return self.form_invalid(form)