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

        # Initialize 4 mock materials in the database
        list = ['Skid','Sling','Pipework','TMMDE']
        for i in range(1, len(list) + 1):
            item = list[i-1]
            material_type = MaterialType.objects.create(id=i,description=item)
            material = Material.objects.create(hal_number=i, hal_description=f'Material {i}', hal_old_number=f'Old Number {i}',material_type=material_type)

    def setUp(self):
        self.mock_skid = Material.objects.get(hal_number=1)
        self.mock_sling = Material.objects.get(hal_number=2)
        self.mock_pipework = Material.objects.get(hal_number=3)
        self.mock_tmmde = Material.objects.get(hal_number=4)

    def test_form_validity(self):
        # Should return skid type
        self.assertEqual(type(self.mock_skid), Material)

        form = GenericInstanceForm({'multifield' : self.mock_skid, 'serial_number' : 12345})
        self.assertTrue(form.is_valid())

    def test_skid_saved_into_db(self):
        form = GenericInstanceForm({'multifield' : self.mock_skid, 'serial_number' : 12345})

        # Is valid method has to be called to save instance into DB
        self.assertTrue(form.is_valid())
        skid_num = SkidInstance.objects.all().count()
        self.assertGreater(skid_num, 0)

        skid = SkidInstance.objects.get(id=form.object_id)
        self.assertEqual(type(skid), SkidInstance)

    def test_sling_saved_into_db(self):
        form = GenericInstanceForm({'multifield' : self.mock_sling, 'serial_number' : 12345})

        # Is valid method has to be called to save instance into DB
        self.assertTrue(form.is_valid())
        sling_num = SlingInstance.objects.all().count()
        self.assertGreater(sling_num, 0)

        sling = SlingInstance.objects.get(id=form.object_id)
        self.assertEqual(type(sling), SlingInstance)

    def test_pipework_saved_into_db(self):
        form = GenericInstanceForm({'multifield' : self.mock_pipework, 'serial_number' : 12345})

        # Is valid method has to be called to save instance into DB
        self.assertTrue(form.is_valid())
        pipe_num = PipeworkInstance.objects.all().count()
        self.assertGreater(pipe_num, 0)

        pipe = PipeworkInstance.objects.get(id=form.object_id)
        self.assertEqual(type(pipe), PipeworkInstance)

    def test_tmmde_saved_into_db(self):
        form = GenericInstanceForm({'multifield' : self.mock_tmmde, 'serial_number' : 12345})

        # Is valid method has to be called to save instance into DB
        self.assertTrue(form.is_valid())
        tmmde_num = TMMDEInstance.objects.all().count()
        self.assertGreater(tmmde_num, 0)

        tmmde = TMMDEInstance.objects.get(id=form.object_id)
        self.assertEqual(type(tmmde), TMMDEInstance)

    def test_form_invalid(self):
        # Testing wrong type of input
        material = "Hello"
        form1 = GenericInstanceForm({'multifield' : material, 'serial_number' : 12345})
        self.assertFalse(form1.is_valid())

        # Testing another scenario of invalid input
        material_type = MaterialType.objects.get(id=1)
        form2 = GenericInstanceForm({'multifield' : material_type, 'serial_number' : 12345})
        self.assertFalse(form1.is_valid())

        # Test for empty serial number
        form3 = GenericInstanceForm({'multifield' : material_type, 'serial_number' : ''})
        self.assertFalse(form1.is_valid())

    def test_login_when_client_not_logged_in(self):
        material = Material.objects.get(hal_number=1)
        response = self.client.get(reverse('core-add-instance'),follow=True)
        self.assertRedirects(response, '{0}?next={1}'.format(reverse('login'), reverse('core-add-instance')))

    def test_login_required_on_add_instance(self):
        # Should return response okay
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post(reverse('core-add-instance'), {'multifield' : self.mock_skid, 'serial_number' : 12345})
        self.assertEqual(response.status_code, 200)









