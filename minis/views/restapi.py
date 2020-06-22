from django.http import JsonResponse

from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from ..filters import (
    GameFilter, FactionFilter, ArmyFilter, UnitFilter, UnitTypeFilter)
from ..models import Game, Faction, Army, Unit, UnitType
from ..serializers import (
    GameSerializer, FactionSerializer, ArmySerializer, UnitSerializer,
    UnitTypeSerializer)


class GameViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    filter_class = GameFilter

    @action(detail=True)
    def get_units_stats(self, request, pk=None):
        units_state_label = []
        units_state_count = []
        for unit_state in Unit.STATE_CHOICES:
            units_state_label.append(
                Unit.get_state_label_by_state_number(unit_state[0]))
            units_state_count.append(Unit.objects.filter(
                state=unit_state[0], army__faction__game_id=pk).count())

        print(units_state_label)
        return JsonResponse(
            {'labels': units_state_label, 'datas': units_state_count})


class FactionViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.CreateModelMixin):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
    filter_class = FactionFilter

    @action(detail=True)
    def get_units_stats(self, request, pk=None):
        units_state_label = units_state_count = []
        unit_state_list = Unit.objects.filter(
            army__faction_id=pk).values_list('state', flat=True).distinct()
        for state in unit_state_list:
            units_state_label.append(Unit.get_state_label_by_state_number(state))
            units_state_count.append(Unit.objects.filter(
                state=state, army__faction_id=pk).count())
        return Response(JSONRenderer().render(
            {'labels': units_state_label, 'datas': units_state_count}))


class ArmyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    queryset = Army.objects.all()
    serializer_class = ArmySerializer
    filter_class = ArmyFilter

    @action(detail=True)
    def get_units_stats(self, request, pk=None):
        units_state_label = units_state_count = []
        unit_state_list = Unit.objects.filter(
            army_id=pk).values_list('state', flat=True).distinct()
        for state in unit_state_list:
            units_state_label.append(Unit.get_state_label_by_state_number(state))
            units_state_count.append(Unit.objects.filter(
                state=state, army_id=pk).count())
        return JsonResponse(
            {'labels': units_state_label, 'datas': units_state_count})


class UnitViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  mixins.CreateModelMixin):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_class = UnitFilter


class UnitTypeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                      mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                      mixins.CreateModelMixin):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    filter_class = UnitTypeFilter
