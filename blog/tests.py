from django.test import TestCase, Client

from .models import Student

# Create your tests here.

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name = ''
        )