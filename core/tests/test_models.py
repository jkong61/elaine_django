from django.test import TestCase
import datetime
from core.models import Material, Instance, NDECertificate

# Create your tests here.
class TestExpiryFunction(TestCase):

    startdate = datetime.date.today() - datetime.timedelta(weeks=52)
    enddate = datetime.date.today() - datetime.timedelta(weeks=1)

    @classmethod
    def setUpTestData(cls):

        print(f'Current start date is {cls.startdate}.')
        print(f'Current end date is {cls.enddate}.')
        print(f'Today\'s date is {datetime.date.today()}.')

        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123')
        instance = Instance.objects.create(id=1,material=material)
        cert = NDECertificate.objects.create(id=1,certificate_number='cert1',validity_start_date=cls.startdate,validity_end_date=cls.enddate,material_instance=instance)

    def test_instance_status(self):
        instance = Instance.objects.get(id=1)
        # should be n
        self.assertNotEqual(instance.status,'e')

    def test_instance_set_expiry_method(self):
        instance = Instance.objects.get(id=1)

        # Method should set instance to be 'e' : Expired
        instance.set_expire()
        self.assertEqual(instance.status,'e')

    def test_nde_expiry_check(self):
        cert = NDECertificate.objects.get(id=1)

        # Instruct cert to check expiry
        cert.checkexpiry()

        instance = Instance.objects.get(id=1)
        self.assertEqual(instance.status,'e')
