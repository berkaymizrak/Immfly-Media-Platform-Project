from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from product import serializers, filters, models

# Create your views here.


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = models.Groups.objects.all()
    serializer_class = serializers.GroupsSerializer
    serializer_action_classes = {
        "detailed": serializers.GroupsDetailedSerializer,
        "detailed_list": serializers.GroupsDetailedSerializer,
    }
    filterset_class = filters.GroupsFilter
    ordering_fields = ()
