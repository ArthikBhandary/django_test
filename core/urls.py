from django.urls import path

from core import views
from allauth.account.views import LoginView
urlpatterns = [
    path("home/", views.ProfileView.as_view(), name="profile"),
    path("", LoginView.as_view(), name="login"),
]