from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
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
    

@method_decorator(login_required, name="dispatch")
class LogoutView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "accounts/logout.html")
    
    
    def post(self, request, *args, **kwargs):
        
        logout(request)
        return redirect("login")