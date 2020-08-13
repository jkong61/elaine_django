from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Material, MaterialType, SkidInstance, TMMDEInstance, SlingInstance, PipeworkInstance
from core.forms import GenericInstanceForm

class TestFormSave(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        material_type = MaterialType.objects.create(description='Skid')
        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123',material_type=material_type)

    def test_form_validity(self):
        # Should return skid type
        material = Material.objects.get(hal_number=123)
        self.assertEqual(type(material), Material)

        form = GenericInstanceForm({'multifield' : material, 'serial_number' : 12345})
        self.assertTrue(form.is_valid())

    def test_item_saved_into_db(self):
        material = Material.objects.get(hal_number=123)
        form = GenericInstanceForm({'multifield' : material, 'serial_number' : 12345})
        skid = SkidInstance.objects.all().count()
        self.assertGreater(skid, 0)


    def test_add_instance_submit(self):
        # Should return skid type
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        material = Material.objects.get(hal_number=123)
        response = self.client.post(reverse('core-add-instance'), {'multifield' : material, 'serial_number' : 12345},follow=True)
        self.assertEqual(response.status_code, 200)






