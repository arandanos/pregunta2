from django.db import models

# Create your models here.
class Test (models.Model):
    _id = models.AutoField(primary_key=True)
    tema = models.TextField()
    
    class Meta:
        verbose_name = ("Test")
        verbose_name_plural = ("Tests")

    def __str__(self):
        return self.tema


class Dificultad(models.Model):
    _id = models.TextField(primary_key=True)  

    class Meta:
        verbose_name = ("Dificultad")
        verbose_name_plural = ("Dificultades")

    def __str__(self):
        return self._id


class Pregunta(models.Model):
    _id = models.AutoField(primary_key=True)
    texto = models.TextField()
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    dificultad = models.ForeignKey('Dificultad', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Pregunta")
        verbose_name_plural = ("Preguntas")

    def __str__(self):
        return self.texto

class Respuesta(models.Model):

    _id = models.AutoField(primary_key=True)
    correcta = models.BooleanField()
    texto = models.TextField()
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Respuesta")
        verbose_name_plural = ("Respuestas")

    def __str__(self):
        return self.texto


