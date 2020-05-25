import django_filters as filters
from django_filters.rest_framework import FilterSet

from .models import Game, Faction, Army, Unit, UnitType


__all__ = [
    'GameFilter', 'FactionFilter', 'ArmyFilter', 'UnitFilter', 'UnitTypeFilter'
]


class  GameFilter(FilterSet):

    class Meta:
        model = Game
        fields = ['name']


class FactionFilter(FilterSet):

    class Meta:
        model = Faction
        fields = ['game', 'name']


class ArmyFilter(FilterSet):

    class Meta:
        model = Army
        fields = ['game', 'faction', 'name']

    game = filters.ModelChoiceFilter(
        field_name='faction__game_id', method="filter_game",
        queryset=Game.objects.all())

    def filter_game(self, queryset, name, value):
        return queryset.filter(faction__game_id=value)


class UnitFilter(FilterSet):

    class Meta:
        model = Unit
        fields = ['game', 'faction', 'army', 'type', 'name']

    game = filters.ModelChoiceFilter(
        field_name='army__faction__game_id', method="filter_game",
        queryset=Game.objects.all())

    def filter_game(self, queryset, name, value):
        return queryset.filter(army__faction__game_id=value)

    faction = filters.ModelChoiceFilter(
        field_name='army__faction_id', method="filter_faction",
        queryset=Faction.objects.all())

    def filter_faction(self, queryset, name, value):
        return queryset.filter(army__faction_id=value)


class UnitTypeFilter(FilterSet):

    class Meta:
        model = UnitType
        fields = ['name', 'unit_type_parent']
