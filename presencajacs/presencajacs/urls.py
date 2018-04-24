"""presencajacs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core import views as core_view, ajax
from secretaria import views as secretaria_views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', core_view.index, name='index'),

    url(r'^entrada/$', core_view.entrada, name='entrada'),

    url(r'^saida/coletiva/$', core_view.saida_coletiva, name='saida_coletiva'),
    url(r'^calcula/tempo/$', core_view.calcula_tempo, name='calcula_tempo'),



    url(r'^secretaria/home/$', secretaria_views.home, name='secretaria_home'),



    url(r'^detalhe/(?P<ra>[0-9]+)/$', secretaria_views.detalhe , name='detalhe'),





]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

