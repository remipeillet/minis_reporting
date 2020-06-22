from rest_framework import serializers

from .models import Game, Faction, Army, Unit, UnitType


__all__ = [
    'GameSerializer', 'FactionSerializer', 'ArmySerializer', 'UnitSerializer',
    'UnitTypeSerializer'
]


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['name', 'order', 'id']


class FactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Faction
        fields = ['game', 'name', 'order', 'id']


class ArmySerializer(serializers.ModelSerializer):

    class Meta:
        model = Army
        fields = ['faction', 'name', 'id']


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ['army', 'name', 'state', 'number_of_minis', 'type', 'id']
        depth = 1


class UnitTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitType
        fields = ['unit_type_parent', 'name', 'id']
