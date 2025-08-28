from django.db import models

class Produto(models.Model):
	nome = models.CharField(max_length=120)
	preco = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	
	def __str__(self):
		return f"{self.nome} (R$ {self.preco:.2f})"

# Create your models here.
