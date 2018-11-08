from rest_framework import serializers
from . import models
class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Mensagem
