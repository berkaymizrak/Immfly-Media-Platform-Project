from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from product import models


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groups
        fields = (
            "id",
            "name",
            "code",
        )


class GroupsDetailedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groups
        fields = (
            "id",
            "name",
            "code",
        )
