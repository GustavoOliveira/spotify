from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import PlayList
from .serialize import PlayListSerializer
from rest_framework.permissions import IsAuthenticated

class PlayListList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer

class PlayListDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer
