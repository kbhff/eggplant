# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class TestMembership(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@food.net'
        )
        self.user.save()

    def test_profile(self):
        resp = self.client.get(reverse('profile'))
        self.assertContains(resp, 'profile', 2, 200)

    def test_user_profile(self):
        self.assertIsNotNone(self.user.userprofile)

    def test_user_profile_privacy(self):
        self.assertFalse(self.user.userprofile.privacy)
