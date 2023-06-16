from rest_framework import serializers
from .models import Field, Reservation


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['id', 'name', 'address', 'contact', 'images', 'price_per_hour', 'location']


class ReservationSerializer(serializers.ModelSerializer):
    total_cost = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'field', 'start_time', 'end_time', 'total_cost']

    def get_total_cost(self, obj):
        return obj.total_cost