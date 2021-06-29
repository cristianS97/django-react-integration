from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Persona

# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

class ListaView(ListView):
    template_name='lista.html'
    model = Persona
    context_object_name='personas'