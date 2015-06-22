# -*- coding: utf-8 -*-
from django.test import TestCase

from django.core.urlresolvers import reverse


class TestDashboard(TestCase):

    def test_home(self):
        response = self.client.get(reverse('dashboard:home'))
        self.assertEqual(response.status_code, 200)
