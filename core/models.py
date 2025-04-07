from django.db import models

# Create your models here.
class Materia(models.Model):
    idMateria = models.AutoField(primary_key=True)
    nomeMateria = models.TextField(max_length=30, null=False)
    
class Assunto(models.Model):
    idAssunto = models.AutoField(primary_key=True)
    nomeAssuntos = models.TextField(max_length=30, null=False)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    
class Aula(models.Model):
    idAula = models.AutoField(primary_key=True)
    nomeAula = models.TextField(max_length=100, null=False)
    url = models.URLField(max_length=150, null=False)
    descricaoAula = models.TextField(max_length=100, null=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    
class Quiz(models.Model):
    idQuiz = models.AutoField(primary_key=True)
    pergunta = models.TextField(max_length=150, null=False)
    resposta = models.TextField(max_length=100, null=False)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    
    
    