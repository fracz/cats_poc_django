from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api.controllers import cats
from api.controllers import token

router = DefaultRouter(trailing_slash=False)
router.register(r'cats', cats.CatViewSet)

urlpatterns = [
    url(r'^token$', token.ObtainJWT.as_view()),
    url(r'', include(router.urls)),
]
