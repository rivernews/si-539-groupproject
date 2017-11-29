from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_data/', views.api_get, name='api_get'),
    url(r'^$', views.index, name='index'),
]