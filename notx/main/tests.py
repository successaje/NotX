from django.test import TestCase, Client
from .views import alertCreate, alertList, alertDetail, alertDelete, alertUpdate
from .models import Alert
import json
from rest_framework import status
from django.urls import reverse
from .serializers import AlertSerializer

from rest_framework.response import Response

# initialize the APIClient app
client = Client()


class CreateAlertTest(TestCase):
    def setUp(self):
        self.valid_payload = {
            'title': 'Unknown Unkowns',
            'product_name': 'Pringles',
            'expiry_date': "27-10-2023",
            "expired": False
        }
        self.invalid_payload = {
            'invalid': 'invalid'
        }

    def test_create_valid_alert(self):
        response = client.post(
            reverse(alertCreate),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_alert(self):
        response = client.post(
            reverse(alertCreate),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AlertListTest(TestCase):
    def setUp(self):
        self.alert_list = reverse(alertList)
    def test_alert_list_GET(self):
        response = self.client.get(self.alert_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AlertDetailTest(TestCase):
    def setUp(self):
        self.test_alert = Alert.objects.create(title='new_alert_title',content='new_alert_content',completed=True)
    def test_alert_detail_GET(self):
        response = client.get(reverse(alertDetail,kwargs={'pk':self.test_alert.pk}))
        alert = Alert.objects.get(pk=self.test_alert.pk)
        serializer = AlertSerializer(alert)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class AlertDeleteTest(TestCase):
    def setUp(self):
        self.test_alert = Alert.objects.create(title='new_alert_title',content='new_alert_content',completed=True)
    def test_alert_delete_DELETE(self):
        response = client.delete(reverse(alertDelete, kwargs={'pk': self.test_alert.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AlertUpdateTest(TestCase):
    def setUp(self):
        self.test_alert = Alert.objects.create(title='new_alert_title',content='new_alert_content',completed=True)
        self.update_payload = {
            'title': 'Updated Unkowns',
            'product_name': 'Updated Pringles',
            'expiry_date': "Updated 27-10-2023",
            "expired": False
        }
    def test_alert_update_POST(self):
        response = client.post(
            reverse(
                alertUpdate,
                kwargs={
                    'pk':self.test_alert.pk
                }
            ),
            data=json.dumps(self.update_payload),
            content_type='application/json'
        )
        self.test_alert.refresh_from_db()
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(self.test_alert.title, 'updated')


class TestAlertModel(TestCase):
    def test_model_str(self):
        title = Alert.objects.create(title='title')
        self.assertEqual(str(title), 'title')