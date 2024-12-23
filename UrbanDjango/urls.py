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

from task2.views import class_template, func_template
from task3.views import task3_platform, task3_games, task3_cart
from task4.views import task4_platform, task4_games, task4_cart

from .views import supermain

urlpatterns = [
        path('', supermain),
        path('admin/', admin.site.urls),
        path('class_template/', class_template.as_view()),
        path('func_template/', func_template),
        path('TemplateView/', TemplateView.as_view(template_name='TemplateView.html')),
        path('platform3/', task3_platform),
        path('platform3/games3/', task3_games),
        path('platform3/cart3/', task3_cart),
        path('platform/', task4_platform),
        path('platform/games/', task4_games),
        path('platform/cart/', task4_cart),
        ]
