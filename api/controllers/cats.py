from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Cat
from api.serializers import CatSerializer
from api.util import worlds_cat_database


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def retrieve(self, request, *args, pk=None):
        if pk == "random":
            return Response({'url': worlds_cat_database.get_random_cat()})
        else:
            return super().retrieve(request, *args, {"pk": pk})
