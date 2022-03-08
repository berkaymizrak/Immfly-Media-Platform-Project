from rest_framework import serializers
from core import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = (
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
        )


class PersonDetailedSerializer(PersonSerializer):
    pass
