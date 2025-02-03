from django.contrib import admin

from .models import EmailVerification


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ["user", "is_verified"]
