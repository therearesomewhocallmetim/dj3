from django.urls import path

from one.views import OneView

urlpatterns = [
    path('hello', OneView.as_view()),
]