from django.test import TestCase, Client
from .views import taskCreate, taskList,taskDetail,taskDelete,taskUpdate
from .models import Task
import json
from rest_framework import status
from django.urls import reverse
from .serializers import TaskSerializer

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

    def test_create_invalid_task(self):
        response = client.post(
            reverse(taskCreate),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TaskListTest(TestCase):
    def setUp(self):
        self.task_list = reverse(taskList)
    def test_task_list_GET(self):
        response = self.client.get(self.task_list)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskDetailTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title',content='new_tast_content',completed=True)
    def test_task_detail_GET(self):
        response = client.get(reverse(taskDetail,kwargs={'pk':self.test_task.pk}))
        task = Task.objects.get(pk=self.test_task.pk)
        serializer = TaskSerializer(task)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class TaskDeleteTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title',content='new_tast_content',completed=True)
    def test_task_delete_DELETE(self):
        response = client.delete(reverse(taskDelete, kwargs={'pk': self.test_task.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TaskUpdateTest(TestCase):
    def setUp(self):
        self.test_task = Task.objects.create(title='new_task_title',content='new_tast_content',completed=True)
        self.update_payload = {
            'title': 'updated',
            'content': 'updated',
            'completed': True
        }
    def test_task_update_POST(self):
        response = client.post(reverse(taskUpdate,kwargs={'pk':self.test_task.pk}),
                               data=json.dumps(self.update_payload),
                               content_type='application/json'
        )
        self.test_task.refresh_from_db()
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(self.test_task.title, 'updated')


class TestTaskModel(TestCase):
    def test_model_str(self):
        title = Task.objects.create(title='title')
        self.assertEqual(str(title), 'title')