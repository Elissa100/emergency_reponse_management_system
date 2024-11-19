from django.contrib.auth.decorators import user_passes_test
from functools import wraps

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'ADMIN':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return _wrapped_view

def responder_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'RESPONDER':
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return _wrapped_view