"""django_openedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views

app_name = 'edu_data'  # to differentiate in the html the application used in the urls
urlpatterns = [
    path('', views.edumaterial_list_view, name='home_page'),
    path('<int:id>', views.detail_page, name='detail'),  # path for going to the detail view
    path('search/', views.search, name='search')  # names need to match the ones in the html to reference url
]
