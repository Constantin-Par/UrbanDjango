from django.shortcuts import render
from django.views.generic import TemplateView


def index1(request):
    return render(request, 'index1.html')

class index(TemplateView):
    template_name = 'second_task/index.html'