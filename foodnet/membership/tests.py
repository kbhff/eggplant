# -*- coding: utf-8 -*-
from django.test import TestCase

from django.core.urlresolvers import reverse


class TestMembership(TestCase):

    def test_profile(self):
        resp = self.client.get(reverse('profile'))
        self.assertContains(resp, 'profile', 2, 200)
