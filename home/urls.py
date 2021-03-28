from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', view=views.index, name = 'index'),
    url(r'^list$', view=views.list_one2many, name = 'list_one2many')
]