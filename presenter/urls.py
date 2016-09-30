from django.conf.urls import url

from .controllers import cats;

urlpatterns = [
    url(r'^cats-in-html$', cats.cats_in_html),
]
