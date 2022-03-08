from core.serializers import LanguageDetailedSerializer
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


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Channel
        fields = (
            "id",
            "code",
            "title",
            "parent",
            "language",
            "group",
            "picture",
        )


class ChannelDetailedSerializer(ChannelSerializer):
    group = GroupsDetailedSerializer(many=True)
    language = LanguageDetailedSerializer()


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = (
            "id",
            "name",
            "description",
            "season",
            "episode",
            "rating",
            "channel",
            "genre",
            "file",
            "person",
        )


class ContentDetailedSerializer(ContentSerializer):
    pass
