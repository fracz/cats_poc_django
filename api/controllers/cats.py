from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Cat
from api.serializers import CatSerializer
from api.util import worlds_cat_database


@api_view(['GET'])
def random(request):
    return Response({'url': worlds_cat_database.get_random_cat()})


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
