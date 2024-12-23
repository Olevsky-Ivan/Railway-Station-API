from django.db import models
from django.contrib.auth.models import User

class Journey(models.Model):
    route = models.ForeignKey("Route", related_name="routes", on_delete=models.CASCADE)
    train = models.ForeignKey("Train", related_name="trainers", on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    class Meta:
        ordering = ["departure_time"]


class Ticket(models.Model):
    cargo = models.IntegerField()
    seat = models.IntegerField()
    journey = models.ForeignKey("Journey", related_name="tickets", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", related_name="tickets", on_delete=models.CASCADE)

    class Meta:
        ordering = ["seat"]


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)


class Train(models.Model):
    name = models.CharField(max_length=87, blank=True)
    cargo_num = models.IntegerField()
    place_in = models.IntegerField()
    train_type = models.ForeignKey("TrainType", related_name="train_types", on_delete=models.CASCADE)

    class Meta:
        ordering = ["place_in"]


class TrainType(models.Model):
    name = models.CharField(max_length=87, blank=True)


class Route(models.Model):
    source = models.ForeignKey("Station", related_name="sources", on_delete=models.CASCADE)
    destination = models.ForeignKey("Station", related_name="destinations", on_delete=models.CASCADE)
    distance = models.IntegerField()

    class Meta:
        ordering = ["distance"]


class Station(models.Model):
    name = models.CharField(max_length=87)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Crew(models.Model):
    first_name = models.CharField(max_length=87)
    last_name = models.CharField(max_length=87)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
