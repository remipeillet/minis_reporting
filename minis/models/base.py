from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = [
    'Game', 'Faction', 'Army', 'Unit', 'UnitType'
]


class Game(models.Model):

    class Meta:
        default_related_name = 'game'
        verbose_name = _("Jeu")
        verbose_name_plural = _("Jeux")
        ordering = ['order']

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_("nom"))
    order = models.PositiveIntegerField(verbose_name=_("ordre"))

    def __str__(self):
        return self.name


class Faction(models.Model):

    class Meta:
        default_related_name = 'faction'
        verbose_name = _("Faction")
        verbose_name_plural = _("Factions")
        ordering = ['order']

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_("nom"))
    order = models.PositiveIntegerField(
        verbose_name=_("ordre"))
    game = models.ForeignKey(
        'Game', models.PROTECT, verbose_name=_("jeu"))

    def __str__(self):
        return self.name


class Army(models.Model):

    class Meta:
        default_related_name = 'army'
        verbose_name = _("Armée")
        verbose_name_plural = _("Armées")

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_("nom"))
    faction = models.ForeignKey(
        'Faction', models.PROTECT, verbose_name=_("faction"))

    def __str__(self):
        return self.name


class Unit(models.Model):

    class Meta:
        default_related_name = 'unit'
        verbose_name = _("Unité")
        verbose_name_plural = _("Unités")
        ordering = ['army', 'state', 'name']

    STATE_CLUSTER = 0
    STATE_ASSEMBLY_READY = 1
    STATE_UNDERCOAT = 2
    STATE_PAINT_WIP = 3
    STATE_MADE_BASE = 4
    STATE_FINISHED = 4
    STATE_CHOICES = [
        (STATE_CLUSTER, _("Sur grappe")),
        (STATE_ASSEMBLY_READY, _("Assemblage")),
        (STATE_UNDERCOAT, _("Sous couché")),
        (STATE_PAINT_WIP, _("Peinture en cours")),
        (STATE_MADE_BASE, _("Soclage")),
        (STATE_FINISHED, _("Terminé")),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_("nom"))
    army = models.ForeignKey(
        'Army', models.PROTECT, verbose_name=_("armée"))
    state = models.PositiveSmallIntegerField(
        verbose_name=_("état"), choices=STATE_CHOICES,
        default=STATE_CLUSTER)
    type = models.ForeignKey(
        'UnitType', models.PROTECT, verbose_name=_("type d'unité"))
    number_of_minis = models.PositiveIntegerField(
        verbose_name=_("nombre de figurines de l'unité"), default=1)

    @classmethod
    def get_state_label_by_stae_number(cls, state):
        dict_of_state = dict(cls.STATE_CHOICES)
        if state in dict_of_state.keys():
            return str(dict(cls.STATE_CHOICES)[state])
        else:
            return ""

    def __str__(self):
        return self.name


class UnitType(models.Model):
    class Meta:
        default_related_name = 'unit_type'
        verbose_name = _("Unité")
        verbose_name_plural = _("Unités")
        ordering = ['name']

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name=_("nom"))
    unit_type_parent = models.ForeignKey(
        'UnitType', models.PROTECT, verbose_name=_("type d'unité parent"),
        null=True, blank=True)

    def __str__(self):
        return self.name
