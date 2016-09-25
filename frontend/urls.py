from django.conf.urls import url
from django.http.response import HttpResponseRedirect

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect('static/index.html')),
]
