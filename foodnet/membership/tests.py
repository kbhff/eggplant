# -*- coding: utf-8 -*-
import datetime

from django.core import mail
from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

from foodnet.common.utils import absolute_url_reverse
from .models import UserProfile, Invitation


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@food.net'
        )
        self.user.set_password('pass')
        self.user.save()
        email_address = EmailAddress.objects\
            .add_email(None, self.user, 'test@food.net', confirm=False,
                       signup=False)
        email_address.verified = True
        email_address.primary = True
        email_address.save()

    def test_profile(self):
        resp = self.client.get(reverse('profile'))
        url = reverse('account_login') + '?next=/membership/profile/'
        self.assertRedirects(resp, url, status_code=302,
                             target_status_code=200, msg_prefix='')

        self.client.login(username='test@food.net', password='pass')
        resp = self.client.get(reverse('profile'))
        expected = '<form action="%s"' % reverse('profile')
        self.assertContains(resp, expected, 1, 200)

        data = {
            'first_name': 'Joe',
            'middle_name': 'Frank',
            'last_name': 'Doe',
            'address': '123 Sunset av. NY, USA',
            'postcode': '123321ABCD',
            'sex': 'f',
            'dob': '11/12/13',
            'privacy': 'checked',
        }
        resp = self.client.post(reverse('profile'), data=data)
        self.assertRedirects(resp, reverse('home'), status_code=302,
                             target_status_code=200, msg_prefix='')

        expected = {
            'middle_name': 'Frank',
            'address': '123 Sunset av. NY, USA',
            'postcode': '123321ABCD',
            'sex': 'f',
            'dob': datetime.date(2013, 11, 12),
            'privacy': True,
        }
        profile = UserProfile.objects.get(user_id=self.user.id)
        self.assertDictContainsSubset(expected, profile.__dict__)
        user = User.objects.get(id=self.user.id)
        self.assertEqual(user.first_name, 'Joe')
        self.assertEqual(user.last_name, 'Doe')

    def test_user_profile(self):
        self.assertIsNotNone(self.user.userprofile)

    def test_user_profile_privacy(self):
        self.assertFalse(self.user.userprofile.privacy)


class TestInvite(TestCase):
    fixtures = [
        'initial_data.json',
    ]

    def setUp(self):
        self.user = User.objects.create(
            username='test_admin',
            email='test_admin@food.net'
        )
        self.user.set_password('pass')
        self.user.save()

    def test_get(self):
        resp = self.client.get(reverse('invite'))
        url = reverse('account_login') + '?next=/membership/invite/'
        self.assertRedirects(resp, url, status_code=302,
                             target_status_code=200, msg_prefix='')

        self.client.login(username='test_admin@food.net', password='pass')
        resp = self.client.get(reverse('invite'))
        self.assertContains(resp, 'invite', 1, 200)

    def test_post(self):
        invited_email = 'test1@localhost'
        data = {
            'division': 1,
            'email': 'test1@localhost',
            'member_category': 1,
        }
        self.client.login(username='test_admin@food.net', password='pass')
        resp = self.client.post(reverse('invite'), data=data, follow=True)
        self.assertRedirects(resp, reverse('home'), status_code=302,
                             target_status_code=200, msg_prefix='')

        expected = ' invitation has been send to {}'.format(invited_email)
        self.assertContains(resp, expected, 1, 200)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'You have been invitate to FoodNet!')

        invitation = Invitation.objects.get(email=invited_email)
        url = absolute_url_reverse('accept_invitation', kwargs=dict(
                                   verification_key=
                                       invitation.verification_key.hex))
        self.assertRegex(invitation.verification_key.hex, r'^[a-z0-9]{32}\Z')
        self.assertIn(url, mail.outbox[0].body)

        self.client.logout()
        accept_invitation_url = reverse('accept_invitation',
                      kwargs=dict(verification_key=
                                  invitation.verification_key.hex))
        resp = self.client.get(accept_invitation_url)

        self.assertContains(resp, 'accept invitation', 2)
        self.assertContains(resp, invitation.verification_key.hex, 1)

        data = {
            'email': 'test1@localhost',
        }
        resp = self.client.post(accept_invitation_url, data=data, follow=True)
        print(resp.content)
        self.assertRedirects(resp, reverse('new_member_set_password'),
                             status_code=302,
                             target_status_code=200, msg_prefix='')
        self.assertContains(resp, 'password1', 3)
        self.assertContains(resp, 'password2', 3)

        # TODO:
        # post to set password
        # check pass
        # redirect to profile
        # check profile
