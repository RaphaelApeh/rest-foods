from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, email= ..., password = ..., **kwargs):
        
        try:
            user = User.objects.get(email=email, is_active=True)
            if all([user.check_password(password), self.user_can_authenticate(user)]):
                return user
            return None
        except User.DoesNotExist:
            return None