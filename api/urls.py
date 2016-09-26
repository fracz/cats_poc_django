from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from api.controllers import cats

router = DefaultRouter(trailing_slash=False)
router.register(r'cats', cats.CatViewSet)

urlpatterns = [
    url(r'^token$', obtain_jwt_token),
    url(r'^cats-in-html$', cats.cats_in_html),
    url(r'^cats/random', cats.random),
    url(r'', include(router.urls)),
]
