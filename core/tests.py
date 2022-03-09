from core import models
from core import factories
from django.test import TestCase

# Create your tests here.


class PersonTestCase(TestCase):
    def setUp(self):
        factories.PersonFactory()

    def test_string_representation(self):
        person = models.Person.objects.first()
        self.assertEqual(str(person), '%s %s' % (person.first_name, person.last_name))
