from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Cat
from api.serializers import CatSerializer
from api.util import worlds_cat_database


def cats_in_html(request):
    cats = Cat.objects.all()
    return render(request, 'api/cats-in-html.html', {'cats': cats})


@api_view(['GET'])
def random(request):
    return Response({'url': worlds_cat_database.get_random_cat()})


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
