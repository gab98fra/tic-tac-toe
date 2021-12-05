from django.urls import path
from api.views import APIInitView, API_TemplateView, DetalleApi, ListAPi, CreateAPI, DetalleAPIView, EliminarAPI


urlpatterns = [
    path('api_list/', API_TemplateView.as_view(), name="api_list"),
    path('api/', APIInitView.as_view(), name="api"),
    path('detalle_api/<int:pk>/', DetalleApi.as_view(), name="detalle_api"),
    path('lista/', ListAPi.as_view(), name="lista_api"),
    path('crear/', CreateAPI.as_view(), name="crear_api"),
    path('detalle/<int:pk>/', DetalleAPIView.as_view(), name="detalle_api"),
    path('eliminar/<int:pk>/', EliminarAPI.as_view(), name="detalle_api"),
]


