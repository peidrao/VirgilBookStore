from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


class LoginRequiredPermission(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home:home"))
        return super().dispatch(request, *args, **kwargs)


class AdministratorPermission(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return
        return super().dispatch(request, *args, **kwargs)
