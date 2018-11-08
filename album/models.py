from django.db import models

# Create your models here.
class Album (models.Model):
    nome= models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    file = models.FileField(blank=False, null=False)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome