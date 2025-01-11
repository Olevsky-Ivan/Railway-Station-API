from django.contrib import admin
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

admin.site.register(Journey)
admin.site.register(Station)
admin.site.register(TrainType)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Route)
admin.site.register(Crew)
admin.site.register(Order)
