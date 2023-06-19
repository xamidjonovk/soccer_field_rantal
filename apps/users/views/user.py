# views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.user import SignupSerializer, SignOutSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


class SigninView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class SignOutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SignOutSerializer

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                pass
        return Response(status=status.HTTP_204_NO_CONTENT)
