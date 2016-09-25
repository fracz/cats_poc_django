from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cats-in-html$', views.cats_in_html),
]
