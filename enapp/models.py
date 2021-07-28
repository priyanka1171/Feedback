from django.db import models

class EnModel(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	phone=models.IntegerField()
	def __str__(self):
		return self.name