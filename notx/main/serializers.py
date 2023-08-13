from rest_framework import serializers
from models import Alert


class AlertSerializer(serializers.Serializer):
    # id = se