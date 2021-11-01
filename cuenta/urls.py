from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import LoginView, logoutView, RedireccionView

urlpatterns = [
    path('', RedireccionView.as_view() , name="redireccion"),
    path('accounts/login/', LoginView.as_view() , name="login"),
    path('logout/', login_required(logoutView), name="logout"),
]

