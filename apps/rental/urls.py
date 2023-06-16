from django.urls import path, include
from rest_framework import routers
from apps.rental.views import FieldViewSet, ReservationViewSet

router = routers.DefaultRouter()
router.register(r'fields', FieldViewSet)
router.register(r'reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
