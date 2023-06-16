from rest_framework.permissions import BasePermission


class IsFieldOwner(BasePermission):
    message = 'You do not have permission to view this field.'

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the field
        return obj.owner == request.user


class IsReservationOwner(BasePermission):
    message = 'You do not have permission to view this reservation.'

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the reservation
        return obj.user == request.user
