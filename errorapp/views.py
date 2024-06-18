from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


"""
when we set debug=False in settings.py then it will look for the 404.html file when 404 error occurs. thus we need to create a 404.html file.
"""