import json
from railway_station.models import (
    Station,
    Crew,
    Train,
    TrainType,
    Ticket,
    Route,
    Order,
    Journey,
)


def load_data():
    with open("postgres_data.json", "r", encoding="utf8") as json_file:
        json_data = json.load(json_file)

    for item in json_data:
        model_name = item["model"]
        fields = item["fields"]

        if model_name == "railway_station.station":
            Station.objects.create(**fields)
        elif model_name == "railway_station.crew":
            Crew.objects.create(**fields)
        elif model_name == "railway_station.train":
            train_type_id = fields["train_type"]
            train_type_instance = TrainType.objects.get(id=train_type_id)
            fields["train_type"] = train_type_instance
            Train.objects.create(**fields)
        elif model_name == "railway_station.traintype":
            TrainType.objects.create(**fields)
        elif model_name == "railway_station.ticket":
            Ticket.objects.create(**fields)
        elif model_name == "railway_station.route":
            Route.objects.create(**fields)
        elif model_name == "railway_station.order":
            Order.objects.create(**fields)
        elif model_name == "railway_station.journey":
            Journey.objects.create(**fields)
