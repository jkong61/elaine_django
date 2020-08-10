from django.test import TestCase
from core.models import Material, Instance, NDECertificate

# Create your tests here.
class TestExpiryFunction(TestCase):
    @classmethod
    def setUpTestData(cls):
        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123')
        Instance.objects.create(id=1,material=material)

    def test_instance_status(self):
        instance = Instance.objects.get(id=1)
        # should be n
        self.assertNotEqual(instance.status,'e')

    def test_instance_set_expiry_method(self):
        instance = Instance.objects.get(id=1)

        # Method should set instance to be 'e' : Expired
        instance.set_expire()
        self.assertEqual(instance.status,'e')