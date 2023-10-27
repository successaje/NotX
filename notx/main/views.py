from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import AlertSerializer
from .models import Alert
# from .permission import IsAuthor

"""

class AlertListAPIView(ListCreateAPIView):

    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(Author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Author=self.request.user)
    
class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    
class AlertDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    lookup_fields = "id"

    # def perform_create(self, serializer):
    #     return serializer.save(Author=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Author=self.request.user)

        
"""



"""

API Overview

"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/alert-list/',
        'Detail View' : '/alert-detail/<str:pk>/',
        'Create' : '/alert-create/',
        'Update' : '/alert-update/<str:pk>/',
        'Delete' : '/alert-delete/<str:pk>/',
    }
    return Response(api_urls)
"""

This function below will show the entire alert repository in the database.

"""
@api_view(['GET'])
def alertList(request):
    alerts = Alert.objects.all()
    serializer = AlertSerializer(alerts, many = True)
    return Response(serializer.data)

"""

This function will show the detailed view of a specific alert with the help of pk.

"""
@api_view(['GET'])
def alertDetail(request, pk):
    alerts = Alert.objects.get(id=pk)
    serializer = AlertSerializer(alerts, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def alertCreate(request):
    if request.method == 'GET':
        alerts = Alert.objects.all()
        serializer = AlertSerializer(alerts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'product_name': request.data.get('product_name'),
            'expiry_date': request.data.get('expiry_date'),
            'expired': request.data.get('expired'),
        }
        serializer = AlertSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def alertUpdate(request, pk):
    alert = Alert.objects.get(id = int(pk))
    serializer = AlertSerializer(instance=alert, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def alertDelete(request, pk):
    alert = Alert.objects.get(id = pk )
    alert.delete()
    return Response("Alert successfully deleted.")
