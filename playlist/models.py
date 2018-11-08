from django.db import models

# Create your models here.
class PlayList (models.Model):
    titulo= models.CharField(max_length=50)
    interprete= models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    letra= models.TextField()
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titulo
        
