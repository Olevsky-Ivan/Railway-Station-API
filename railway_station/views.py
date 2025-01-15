from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from railway_station.models import (
    Journey,
    Station,
    TrainType,
    Train,
    Ticket,
    Route,
    Crew,
    Order
)

from railway_station.serializers import (
    JourneySerializer,
    StationSerializer,
    TrainTypeSerializer,
    TrainSerializer,
    TicketSerializer,
    RouteSerializer,
    CrewSerializer,
    OrderSerializer,
)


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [IsAuthenticated]


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [IsAuthenticated]


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]


class TrainTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = [IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [IsAuthenticated]


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
