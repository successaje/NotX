from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlertListAPIView.as_view(), name = "alerts"),
    path('<int:id>', views.AlertDetailAPIView.as_view(), name = "alert"),
]
