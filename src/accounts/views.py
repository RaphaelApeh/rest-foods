from django.views.generic import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth import (
    login,
    logout,
    authenticate,
    get_user_model
)

from .forms import (
    LoginForm
)
from .decorator import redirect_login_user


@method_decorator(redirect_login_user, name="dispatch")
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

            return super().form_valid(form)
        return self.form_invalid(form)