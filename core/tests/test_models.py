from django.test import TestCase
import datetime
from core.models import Material, PipeworkInstance, MaterialType

# Create your tests here.
class TestExpiryFunction(TestCase):

    startdate = datetime.date.today() - datetime.timedelta(weeks=52)
    enddate = datetime.date.today() - datetime.timedelta(weeks=1)

    @classmethod
    def setUpTestData(cls):

        print(f'Current start date is {cls.startdate}.')
        print(f'Current end date is {cls.enddate}.')
        print(f'Today\'s date is {datetime.date.today()}.')

        # Certificate is expired by default by 1 week
        material_type = MaterialType.objects.create(description='hello')
        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123',material_type=material_type)
        instance = PipeworkInstance.objects.create(id=1,material=material)        

    def test_instance_status(self):
        instance = PipeworkInstance.objects.get(id=1)
        # should be n
        self.assertNotEqual(instance.status,'e')

    def test_instance_set_expiry_method(self):
        instance = PipeworkInstance.objects.get(id=1)

        # Method should set instance to be 'e' : Expired
        instance.set_expire()
        self.assertEqual(instance.status,'e')

    def test_get_instance_material_type(self):
        material_type = MaterialType.objects.get(id=1)
        instance = PipeworkInstance.objects.get(id=1)
        mtl_type = instance.get_instance_type()
        self.assertEqual(material_type, mtl_type)