from django.test import TestCase

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Test model', content='hope it works')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'Test model')
    
    def test_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.content}'
        self.assertEquals(expected_object_name, 'hope it works')
