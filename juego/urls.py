from django.urls import path
from .views import HomeView, JuegoView, EstadisticasView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomeView.as_view()), name="home"),
    path('partida/<int:pk>/', login_required(JuegoView.as_view()), name="partida_juego"),
    path('estadisticas/', login_required(EstadisticasView.as_view()), name="estadisticas"),
]