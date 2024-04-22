from django.test import TestCase
from django.urls import reverse
from .models import Task
from .forms import TaskForm

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(title="Sample Task", description="Sample Description", completed=False)

    
    def testTaskShouldBeCreatedSuccefullywithNotCompletedStatus(self):
        self.assertEqual(self.task.title, "Sample Task")
        self.assertEqual(self.task.description, "Sample Description")
        self.assertFalse(self.task.completed)

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), self.task.title)


class TaskListViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="List View Task", description="List Test", completed=True)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)



# class TaskFormTest(TestCase):
#     def test_form_validity(self):
#         form_data = {'title': 'New Task', 'description': 'Do something', 'completed': False}
#         form = TaskForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         form.save()
#         self.assertEqual(Task.objects.count(), 1)

