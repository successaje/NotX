from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import AlertSerializer
from .models import Alert
# from .permission import IsAuthor

class AlertListAPIView(ListCreateAPIView):

    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(Author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Author=self.request.user)

class EssayDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_fields = "id"

    # def perform_create(self, serializer):
    #     return serializer.save(Author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Author=self.request.user)


