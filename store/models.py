# coding: utf8
from __future__ import unicode_literals

from django.db import models


class Selling(models.Model):

    class Meta:
        verbose_name = u'Продажа'
        verbose_name_plural = u'Продажи'

    data = models.DateField(
        verbose_name=u'Дата продажи',
        auto_now=True,
    )
    tare_number = models.PositiveIntegerField(
        verbose_name=u'Номер тары',
    )
    value = models.DecimalField(
        verbose_name=u'Объем',
        max_digits=5,
        decimal_places=2,
    )
    number_pumping = models.PositiveIntegerField(
        verbose_name=u'Номер откачки',
    )
    honey_type = models.CharField(
        verbose_name=u'Мёд',
        max_length=32,
    )
    kind = models.PositiveSmallIntegerField(
        verbose_name=u'Тип сделки',
        choices={
            (0, 'Подарок'),
            (1, 'Купил'),
            (2, 'Для себя'),
        }
    )
    weight = models.DecimalField(
        verbose_name=u'Вес',
        max_digits=5,
        decimal_places=2,
    )
    cost = models.DecimalField(
        verbose_name=u'Цена',
        max_digits=8,
        decimal_places=2,
    )
    payment = models.DecimalField(
        verbose_name=u'Оплата',
        max_digits=8,
        decimal_places=2,
    )
