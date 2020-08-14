from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Material, MaterialType

class TestFormSave(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        material_type = MaterialType.objects.create(description='Skid')
        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123',material_type=material_type)

    def test_login_when_client_not_logged_in(self):
        response = self.client.get(reverse('core-add-instance'),follow=True)
        self.assertRedirects(response, '{0}?next={1}'.format(reverse('login'), reverse('core-add-instance')))

    def test_login_required_on_add_instance(self):
        # Should return response okay
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        material = Material.objects.get(hal_number=123)
        response = self.client.post(reverse('core-add-instance'), {'multifield' : material, 'serial_number' : 12345})
        self.assertEqual(response.status_code, 200)









