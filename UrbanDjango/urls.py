"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from example1.views import index
from example1.views import index1

from task2.views import class_template
from task2.views import func_template


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index.as_view()), # через класс
        path('index1/', index1), # через функцию
        path('index2/', TemplateView.as_view(template_name='index2.html')),  # через TemplateView
        path('class_template/', class_template.as_view()),
        path('func_template/', func_template),
        path('TemplateView/', TemplateView.as_view(template_name='second_task/TemplateView.html')),
        ]
