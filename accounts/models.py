from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser): # herda o model User base padrão do Django
    data_nascimento = models.fields.DateField("Data de Nascimento", null=True, blank=True)
    cpf = models.fields.CharField("CPF", max_length=11, null=True, blank=True)
    imagem = models.FileField(
        upload_to='images',
        default=None,
        null=True
    )


