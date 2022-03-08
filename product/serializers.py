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
    deepest_channel = serializers.SerializerMethodField()

    class Meta:
        model = models.Channel
        fields = (
            'id',
            'code',
            'title',
            'parent',
            'language',
            'group',
            'picture',
            'content_set',
            'deepest_channel',
        )

    def get_deepest_channel(self, obj):
        return not obj.channel_set.all().exists()


class ChannelDetailedSerializer(ChannelSerializer):
    group = GroupsDetailedSerializer(many=True)
    language = LanguageDetailedSerializer()
    parent = ChannelSerializer()
    content_set = ContentDetailedSerializer(many=True)
