from apps.users.views.user import SignupView, SigninView, SignOutView
from django.urls import path

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
]