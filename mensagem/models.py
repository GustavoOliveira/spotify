from django.db import models

# Create your models here.
class Mensagem (models.Model):
    usuario = models.CharField(max_length=50)
    assunto = models.CharField(max_length=50)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.assunto
        
