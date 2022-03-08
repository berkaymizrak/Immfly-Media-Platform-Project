from core.serializers import LanguageDetailedSerializer, PersonDetailedSerializer, DocumentDetailedSerializer
from rest_framework import serializers
from product import models


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groups
        fields = (
            'id',
            'name',
            'code',
        )


class GroupsDetailedSerializer(GroupsSerializer):
    pass


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = (
            'id',
            'name',
            'age_rate',
        )


class GenreDetailedSerializer(GenreSerializer):
    pass


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Content
        fields = (
            'id',
            'name',
            'description',
            'season',
            'episode',
            'rating',
            'channel',
            'genre',
            'file',
            'person',
            'get_age_rate',
        )


class ContentPersonDetailedSerializer(serializers.ModelSerializer):
    person = PersonDetailedSerializer()

    class Meta:
        model = models.Content.person.through
        fields = (
            'id',
            'content',
            'person',
            'relation_type',
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['relation_type'] = instance.relation_type and instance.get_relation_type_display()
        return representation


class ContentDetailedSerializer(ContentSerializer):
    person = ContentPersonDetailedSerializer(source='contentpersonrelation_set', many=True, )
    genre = GenreDetailedSerializer(many=True)
    file = DocumentDetailedSerializer(many=True)


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
            'get_author_list',
            'content_set',
            'deepest_channel',
            'get_rating',
        )

    def get_deepest_channel(self, obj):
        return not obj.channel_set.all().exists()


class ChannelDetailedSerializer(ChannelSerializer):
    group = GroupsDetailedSerializer(many=True)
    language = LanguageDetailedSerializer()
    parent = ChannelSerializer()
    content_set = ContentDetailedSerializer(many=True)
