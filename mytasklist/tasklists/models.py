# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

STATUS_PENDENTE = 'p'
STATUS_CONCLUIDO = 'c'
STATUS_CHOICES = (
    (STATUS_PENDENTE,_(u'Pendente')),
    (STATUS_CONCLUIDO,_(u'Concluído'))
)

class Tasks(models.Model):
    """
        autor: Carlos Arruda
        criado em: 03/2019
    """
    titulo = models.CharField(max_length=30, unique=True)
    descricao = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    atualizado_em = models.DateTimeField(null=True)
    atualizado_por = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='+')
    excluido_em = models.DateField(null=True)

    def __str__(self):
        return self.titulo