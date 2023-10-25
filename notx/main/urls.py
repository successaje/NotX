from django.urls import path

from . import views

urlpatterns = [
    path('', views.apiOverview.as_view(), name = "alerts"),
    path('alert-list/', views.alertList, name="alert-list"),
    path('alert-detail/<str:pk>/', views.alertDetail, name="alert-Detail"),
    path('alert-create/', views.alertCreate, name="alert-Create"),
    path('alert-update/<str:pk>/', views.alertUpdate, name="alert-update"),
    path('alert-delete/<str:pk>/', views.alertDelete, name="alert-delete"),
]
