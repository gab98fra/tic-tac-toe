from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from cuenta.forms import FormularioLogin


class RedireccionView(View):
    """Redirecciona al cuadro de login
        
        
        :View:Vista django basado en clases
    """
    
    def get(self, request, *args, **kwargs):

        return redirect("login")
        

class LoginView(FormView):
    """Inicio de sesión


        :FormView:Vista formulario django
    """
    
    template_name="cuenta/login.html"
    form_class=FormularioLogin
    success_url=reverse_lazy("home")

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


def logoutView(request):
    "Finalizar sesión"
    
    logout(request)
    return redirect("login")
