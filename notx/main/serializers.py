from rest_framework import serializers
from .models import Alert
# from ..accounts.models import User


class AlertSerializer(serializers.Serializer):
    class Meta:
        model = Alert
        fields = '__all__'

        def validate(self, attrs):
            pass

        # def __init__(self, attrs)