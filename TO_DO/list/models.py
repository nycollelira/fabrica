from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefas(models.Model):
    usuário = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    título = models.CharField(max_length=200)
    descrição = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    criar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.título
    
class Meta:
    ordering = ['completo']
    
