from django.db.models import Q
from rest_framework import viewsets, filters
from django_filters import rest_framework as df_filters
from django.contrib.gis.db.models.functions import Distance

from rest_framework.permissions import IsAuthenticated
from rolepermissions.checkers import has_role
from ..models import Field
from ..serializers import FieldSerializer
from apps.users.permissions import IsFieldOwner


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    filter_backends = [filters.OrderingFilter, df_filters.DjangoFilterBackend]
    ordering_fields = ['location']

    def get_permissions(self):
        if self.action == 'create' or has_role(self.request.user, 'admin'):
            return [IsAuthenticated()]
        else:
            return [IsFieldOwner(), IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.location:
            user_location = user.location
            queryset = Field.objects.annotate(distance=Distance('location', user_location)).order_by('distance')
        else:
            queryset = Field.objects.all()

        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')

        # Check if both start_time and end_time are provided
        if start_time and end_time:
            # Filter fields based on reservations falling within the specified time range
            queryset = queryset.filter(
                ~Q(reservation__start_time__lt=end_time, reservation__end_time__gt=start_time)
            )
        return queryset
