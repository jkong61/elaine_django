import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TestAjaxAPI(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()


    def test_ajax_api_with_get(self):
        response = self.client.get(reverse('inspection-ajax-api'))
        self.assertEqual(response.status_code, 404)

    def test_ajax_api_with_get_logged_in(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('inspection-ajax-api'))
        self.assertEqual(response.status_code, 404)

    def test_ajax_api_with_get_logged_in(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        data = json.dumps({"data": "Mock data"})
        response = self.client.post(reverse('inspection-ajax-api'),
            data=data,
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

    def test_ajax_api_with_get_logged_in(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        data = json.dumps({"data": "skid"})
        response = self.client.post(reverse('inspection-ajax-api'),
            data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
