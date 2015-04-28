# -*- coding: utf-8 -*-
from django.test import TestCase

from django.core.urlresolvers import reverse


class TestDashboard(TestCase):

    def test_home(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'dashboard', 2, 200)
