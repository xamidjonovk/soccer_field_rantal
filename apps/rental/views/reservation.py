from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rolepermissions.checkers import has_role
from ..models import Field, Reservation
from ..serializers import ReservationSerializer
from apps.users.permissions import IsReservationOwner


class ReservationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action == 'create' or has_role(self.request.user, 'admin'):
            return [IsAuthenticated()]
        else:
            return [IsReservationOwner(), IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or has_role(self.request.user, 'admin'):
            queryset = Field.objects.all()
        else:
            queryset = Field.objects.filter(owner=self.request.user)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
