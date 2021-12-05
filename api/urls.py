from django.urls import path
from api.views import APIView, API_TemplateView, DetalleApi


urlpatterns = [
    path('api_list/', API_TemplateView.as_view(), name="api_list"),
    path('api/', APIView.as_view(), name="api"),
    path('detalle_api/<int:pk>/', DetalleApi.as_view(), name="detalle_api"),
]
