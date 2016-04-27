from django.conf.urls import url
from . import views

urlpatterns = [
    # el simbolo '$' quiere decir que ese va a ser el index de la pagina
    url(r'^$', views.index, name='patricia vicuna'),
]
