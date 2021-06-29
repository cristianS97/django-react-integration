from django.urls import path
from .views import IndexView, ListaView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('personas', ListaView.as_view(), name='personas')
]
