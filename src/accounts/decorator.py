from django.conf import settings
from django.http import HttpResponseRedirect


def redirect_login_user(view_func):

    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return view_func(request, *args, **kwargs)
    
    return wrap
