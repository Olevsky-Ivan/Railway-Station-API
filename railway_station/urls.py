from django.urls import path, include
from rest_framework.routers import DefaultRouter
from railway_station.views import (
    TicketViewSet,
    CrewViewSet,
    OrderViewSet,
    RouteViewSet,
    TrainViewSet,
    StationViewSet,
    JourneyViewSet,
    TrainTypeViewSet,
)


router = DefaultRouter()
router.register(r"tickets", TicketViewSet, basename="ticket")
router.register(r"crews", CrewViewSet, basename="crew")
router.register(r"orders", OrderViewSet, basename="order")
router.register(r"routes", RouteViewSet, basename="route")
router.register(r"trains", TrainViewSet, basename="train")
router.register(r"stations", StationViewSet, basename="station")
router.register(r"journeys", JourneyViewSet, basename="journey")
router.register(r"train-types", TrainTypeViewSet, basename="train-type")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "railway_station"
