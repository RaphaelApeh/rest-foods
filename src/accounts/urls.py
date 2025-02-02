from django.urls import path

from .views import (
    LoginView,
    LogoutView,
    SignupView,
    EmailVerificationView
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("verify-email/", EmailVerificationView.as_view(), name="verify-email")
]