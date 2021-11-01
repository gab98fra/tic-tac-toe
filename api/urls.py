from django.urls import path
from api.views import PartidaView, API_TemplateView


urlpatterns = [
    path('partida_api/', PartidaView.as_view(), name="partida_api"),
    path('partida_api_list/', API_TemplateView.as_view(), name="partida_api_list"),

]