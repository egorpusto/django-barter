from django.test import TestCase
from django.contrib.auth.models import User
from .models import Ad

class AdModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.ad = Ad.objects.create(
            user=self.user,
            title='Книга',
            description='Старое издание',
            category='Книги',
            condition='used'
        )

    def test_ad_creation(self):
        self.assertEqual(str(self.ad), 'Книга')
        self.assertEqual(self.ad.condition, 'used')
