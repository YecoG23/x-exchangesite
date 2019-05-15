from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

#GENERAL TEMPLATE VIEW INDEX
class IndexView(TemplateView):
    template_name = 'index.html'
