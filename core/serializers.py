from rest_framework import serializers
from core import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
        )


class PersonDetailedSerializer(PersonSerializer):
    pass


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Document
        fields = (
            'id',
            'document',
            'doc_type',
        )


class DocumentDetailedSerializer(DocumentSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['doc_type'] = instance.doc_type and instance.get_doc_type_display()
        return representation


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = (
            'id',
            'name',
            'code',
        )


class LanguageDetailedSerializer(LanguageSerializer):
    pass
