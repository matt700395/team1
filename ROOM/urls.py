"""ROOM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accountapp.views import AccountIndexView
from roomapp.views import RoomIndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AccountIndexView.as_view(), name='index'),

    path('test/', RoomIndexView.as_view(), name='roomlist'),

    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('boards/', include('boardapp.urls')),
    path('rooms/', include('roomapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('reviews/', include('reviewapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)