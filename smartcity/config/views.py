from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, mixins

from django.shortcuts import get_object_or_404

from .models import Config
from .serializers import ConfigSerializer

class ConfigListCreateAPIView(generics.ListCreateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

config_list_create_api_view = ConfigListCreateAPIView.as_view()

class ConfigDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

config_detail_api_view = ConfigDetailAPIView.as_view()

class ConfigUpdateAPIView(generics.UpdateAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

config_update_api_view = ConfigUpdateAPIView.as_view()

class ConfigDeleteAPIView(generics.DestroyAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer

config_delete_api_view = ConfigDeleteAPIView.as_view()