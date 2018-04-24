from django.db import models



class Aluno(models.Model):

	ra = models.IntegerField()
	nome = models.CharField(max_length=100)
	email = models.CharField(max_length=200, blank=True, null=True)
	fase = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return self.nome


class Presenca(models.Model):

	ra = models.IntegerField()
	nome = models.CharField(max_length=100, default='', blank=True, null=True)
	fase = models.IntegerField(default=0)
	email = models.CharField(max_length=200, blank=True, null=True)
	data_hora_entrada = models.DateTimeField(auto_now_add=True)
	data_hora_saida = models.DateTimeField(blank=True, null=True)
	tempo = models.TimeField(blank=True, null=True, max_length=100)



	def __str__(self):
		return self.nome



