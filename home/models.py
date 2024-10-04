from django.db import models

# Create your models here.
class Myfile(models.Model):
    title = models.CharField(max_length=20)
    arquivo = models.FileField(upload_to="img")# colocando na pasta escolhida   no caso sera img, pois havera outras medias no projeto

    def __str__(self) -> str:
        return self.title