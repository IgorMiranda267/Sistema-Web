from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import CustomUser

def user_has_permission(permission_codename):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.has_perm(permission_codename):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Você não tem permissão para acessar esta página.")
        return _wrapped_view
    return decorator
