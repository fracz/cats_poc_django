from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.views.static import serve

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect('index.html')),
    url(r'^(?P<path>.*)$', serve, {'document_root': 'static/files'}),
]
