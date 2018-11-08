from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Mensagem
from .serialize import MensagemSerializer

class MensagemList(generics.ListCreateAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class MensagemDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
