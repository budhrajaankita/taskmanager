from django.urls import reverse
from django.test import TestCase
from .models import Task

class TaskTests(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            priority=2,
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'Test Description')
        self.assertEqual(task.priority, 2)

