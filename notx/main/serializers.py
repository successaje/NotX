from rest_framework import serializers
from models import Alert
from ..accounts.models import User


class AlertSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "title", "product_name", "expiry_date", "batch_no"
        ]

        def validate(self, attrs):
            pass

        # def __init__(self, attrs)