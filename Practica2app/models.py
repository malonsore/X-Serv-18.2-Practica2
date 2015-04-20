from django.db import models

# Create your models here.

class Practica2appData(models.Model):
	larga = models.CharField(max_length=200)
	corta = models.CharField(max_length=200)
