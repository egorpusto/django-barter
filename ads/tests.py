from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Ad, ExchangeProposal
from django.urls import reverse


class AdTestCase(TestCase):
    def setUp(self):
        # Create test user and another user
        self.user = User.objects.create_user(
            username='user1', password='testpass')
        self.other_user = User.objects.create_user(
            username='user2', password='testpass')

        # Create ad for user1
        self.ad = Ad.objects.create(
            user=self.user,
            title='Book',
            description='A good book',
            category='Books',
            condition='used'
        )

    def test_ad_creation(self):
        # Test if ad is created correctly
        self.assertEqual(self.ad.title, 'Book')
        self.assertEqual(str(self.ad), 'Book')

    def test_ad_edit_permission(self):
        # Only author can edit ad
        c = Client()
        c.login(username='user2', password='testpass')
        response = c.get(reverse('ad_edit', args=[self.ad.pk]))
        self.assertEqual(response.status_code, 403)

    def test_ad_delete_permission(self):
        # Only author can delete ad
        c = Client()
        c.login(username='user2', password='testpass')
        response = c.post(reverse('ad_delete', args=[self.ad.pk]))
        self.assertEqual(response.status_code, 403)

    def test_ad_filter(self):
        # Check filtering by category
        ads = Ad.objects.filter(category__icontains='Books')
        self.assertEqual(len(ads), 1)

    def test_exchange_proposal(self):
        # Create ad for other user
        ad2 = Ad.objects.create(
            user=self.other_user,
            title='Lamp',
            description='A desk lamp',
            category='Electronics',
            condition='new'
        )

        # Create exchange proposal
        proposal = ExchangeProposal.objects.create(
            ad_sender=self.ad,
            ad_receiver=ad2,
            comment='Want to exchange my book for your lamp.'
        )

        # Test proposal creation
        self.assertEqual(proposal.status, 'pending')

        # Change status
        proposal.status = 'accepted'
        proposal.save()
        self.assertEqual(proposal.status, 'accepted')
