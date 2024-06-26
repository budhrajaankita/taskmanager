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


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_lists_all_tasks(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('List View Task', response.content.decode())


class TaskFormTest(TestCase):
    def test_valid_data(self):
        form = TaskForm({
            'title': "Form Validity",
            'description': "Test form Validity",
            'completed': False
        })
        self.assertTrue(form.is_valid())
#         form.save()
#         self.assertEqual(Task.objects.count(), 1)


    def test_taskcount(self):
        form = TaskForm({
            'title': "Task count",
            'description': "Test task count increase",
            'completed': False
        })
        form.save()
        self.assertEqual(Task.objects.count(), 1)
    

    def test_form_blank_data(self):
        form = TaskForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class TaskUpdateTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Test Task", description="Update Test Description", completed=True)

    def test_task_update_view(self):
        response = self.client.post(reverse('task_update', args=[self.task.id]), {
            'title': "Updated Title",
            'description': self.task.description,
            'completed': self.task.completed
        })
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Title")

class TaskDeleteTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Delete Test Task", description="Delete Test Description", completed=False)

    def test_task_delete_view(self):
        self.assertEqual(Task.objects.count(), 1)
        response = self.client.post(reverse('task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)