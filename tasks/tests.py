from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    
    def taskShouldBeCreatedSuccefullywithNotCompletedStatus(self):
        task = Task.objects.create(title="Sample Task", description="Sample Description", completed=False)
        self.assertEqual(task.title, "Sample Task")
        self.assertEqual(task.description, "Sample Description")
        self.assertFalse(task.completed)
