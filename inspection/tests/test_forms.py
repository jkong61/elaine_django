from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

class TestSaveInstanceForms(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_form_instance_render(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('inspection-calibration'))
        self.assertEqual(response.status_code, 200)

