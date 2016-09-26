from rest_framework import serializers

from api.models import Cat
from api.util.epoch_field import UnixEpochDateField


class CatSerializer(serializers.ModelSerializer):
    creator = serializers.CharField(required=False)
    created = UnixEpochDateField(required=False)

    class Meta:
        model = Cat
        fields = ('id', 'url', 'creator', 'created')
