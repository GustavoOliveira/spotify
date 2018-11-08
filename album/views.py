from django.shortcuts import render
from rest_framework import generics
from .models import Album
from .serialize import AlbumSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


class AlbumList(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = AlbumSerializer

    def post(self, request, *args, **kwargs):
        albumSerializer = AlbumSerializer(data=request.data)
        if albumSerializer.is_valid():
            albumSerializer.save()
            return Response(albumSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(albumSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = Album.objects.all()
        albumSerializer = AlbumSerializer(queryset, many=True)
        return Response(albumSerializer.data)


class AlbumDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
