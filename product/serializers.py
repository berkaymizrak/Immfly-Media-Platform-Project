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


class GroupsDetailedSerializer(GroupsSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = (
            "id",
            "name",
            "age_rate",
        )


class GenreDetailedSerializer(GenreSerializer):
    pass
