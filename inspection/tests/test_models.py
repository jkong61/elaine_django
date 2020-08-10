from django.test import TestCase
import datetime
from core.models import Material, Instance, VisualInspection

# Create your tests here.
class TestExpiryFunction(TestCase):

    startdate = datetime.date.today() - datetime.timedelta(weeks=52)
    enddate = datetime.date.today() - datetime.timedelta(weeks=1)

    @classmethod
    def setUpTestData(cls):
        # Certificate is expired by default by 1 week
        material = Material.objects.create(hal_number='123', hal_description='Some material', hal_old_number='qwerty123')
        instance = Instance.objects.create(id=1,material=material)
        cert = VisualInspection.objects.create(id=1,validity_start_date=cls.startdate,validity_end_date=cls.enddate,material_instance=instance)

    def test_nde_expiry_check(self):
        cert = VisualInspection.objects.get(id=1)

        # Instruct cert to check expiry
        cert.checkexpiry()

        instance = Instance.objects.get(id=1)
        self.assertEqual(instance.status,'e')

    def test_nde_timeleft(self):
        cert = VisualInspection.objects.get(id=1)

        # Override expiry date to be more than today's date
        cert.validity_end_date = datetime.date.today() + datetime.timedelta(weeks=1)

        self.assertGreater(cert.validity_end_date, datetime.date.today())
        # print(cert.get_time_left_days())

    def test_nde_warning(self):
        cert = VisualInspection.objects.get(id=1)

        # Override expiry date to be more than today's date ,by 12 weeks (3 months)
        cert.validity_end_date = datetime.date.today() + datetime.timedelta(weeks=12)
        cert.checkexpiry()
        self.assertEqual(cert.get_reference_material().status,'n')

        # Override expiry date to be more than today's date by 5 weeks (within 6 week warning)
        cert.validity_end_date = datetime.date.today() + datetime.timedelta(weeks=5)
        cert.checkexpiry()

        # Instance should be set to warning, and not expired yet
        self.assertNotEqual(cert.get_reference_material().status,'e')
        self.assertEqual(cert.get_reference_material().status,'w')

    def test_nde_get_reference(self):
        cert = VisualInspection.objects.get(id=1)
        instance = Instance.objects.get(id=1)

        self.assertEqual(instance, cert.get_reference_material())

