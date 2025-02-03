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
    RegisterForm,
    EmailVerificationForm
)
from .decorators import redirect_login_user
from .models import EmailVerification

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
        messages.error(self.request, "No user with this email and password or user is inactive.")
        return self.form_invalid(form)
    

@method_decorator(login_required, name="dispatch")
class LogoutView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "accounts/logout.html")
    
    
    def post(self, request, *args, **kwargs):
        
        logout(request)
        messages.success(self.request, "Logged out successfully.")
        return redirect("login")
    
@method_decorator(redirect_login_user, name="dispatch")
class SignupView(FormView):
    template_name = "accounts/signup.html"
    form_class = RegisterForm
    success_url = "/accounts/verify-email/"

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data["email"]
        self.request.session["email"] = email
            
        return super().form_valid(form)


class EmailVerificationView(FormView):
    
    template_name = "accounts/verify-email.html"
    form_class = EmailVerificationForm
    
    success_url = "/accounts/login"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated or request.user.is_active:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        verification_code = form.cleaned_data["verification_code"]
        email = self.request.session.get("email")
        if email is None:
            return redirect("login")
        user = User.objects.get(email__iexact=email)
        _email = EmailVerification.objects.filter(user=user)
        if _email.count() > 1:
            messages.error(self.request, "Invaild data.")
            return redirect("verify-email")
        email_instance = _email.get()
        if email_instance.verification_code == verification_code:
            email_instance.is_verified = True
            email_instance.save()
            if email_instance.is_verified:
                user.is_active = True
                user.save()
            self.request.session.flush()
            messages.success(self.request, "Account activated successfully.")
            return super().form_valid(form)
        else:
            messages.error(self.request, "Invalid verification code.")
            return redirect("verify-email")