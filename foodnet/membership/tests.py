# -*- coding: utf-8 -*-
import os
import datetime

from django.core import mail
from django.conf import settings
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from allauth.account.models import EmailAddress

from foodnet.common.utils import absolute_url_reverse
from .models import (UserProfile, Invitation, Member, Department,
                     MemberCategory, DepartmentCategory, DepartmentMembership)
from django.test.utils import override_settings


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
            'city': 'New York',
            'tel': '79231232',
            'sex': 'f',
            'date_of_birth': '11/12/13',
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
            'city': 'New York',
            'tel': '79231232',
            'date_of_birth': datetime.date(2013, 11, 12),
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

    def test_user_member_department_models(self):
        # Although this may look like testing ORM API I thought it
        # would be good to just write a test to show how we expect
        # membership to work
        member_cat = MemberCategory.objects.create(name='household')
        member = Member.objects.create(category=member_cat,
                                       number=12345)
        user2 = User.objects.create(
            username='testuser2',
            email='test2@food.net'
        )
        # Member is a set of users (user profiles)
        # - eg. a house with one address
        member.userprofile_set.add(self.user.userprofile)
        member.userprofile_set.add(user2.userprofile)
        self.assertEqual(2, member.userprofile_set.all().count())

        dept_cat = DepartmentCategory.objects.create(name='large')
        dept = Department.objects.create(category=dept_cat, name='super dept')

        # Department membership is a group of members
        membership = DepartmentMembership.objects.create(member=member,
                                                         department=dept)

        # we dont't have to have a fresh copy of dept
        self.assertEqual(1, dept.members.all().count())
        self.assertEqual(1, member.department_set.all().count())
        dept.members.clear()
        self.assertEqual(0, dept.members.all().count())
        self.assertEqual(0, member.department_set.all().count())


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
        self.user.is_superuser = True

        content_type = ContentType.objects.get_for_model(Invitation)
        can_invite = Permission.objects.get(content_type=content_type,
                                            codename='can_invite')
        self.user.user_permissions.add(can_invite)
        self.user.save()
        os.environ['RECAPTCHA_TESTING'] = 'True'

    def test_get(self):
        resp = self.client.get(reverse('invite'))
        url = reverse('account_login') + '?next=/membership/invite/'
        self.assertRedirects(resp, url, status_code=302,
                             target_status_code=200, msg_prefix='')

        self.client.login(username='test_admin@food.net', password='pass')
        resp = self.client.get(reverse('invite'))
        print(resp.content)
        self.assertContains(resp, 'invite', 1, 200)

    def test_user_already_verified(self):
        invited_email = 'test_admin@food.net'
        data = {
            'department': 1,
            'email': invited_email,
            'member_category': 1,
        }
        self.client.login(username='test_admin@food.net', password='pass')
        resp = self.client.post(reverse('invite'), data=data, follow=True)
        expected = 'User {} already exists'.format(invited_email)
        self.assertContains(resp, expected, 1, 200)

    def test_send_invitation(self):
        invited_email = 'test1@localhost'
        data = {
            'department': 1,
            'email': 'test1@localhost',
            'member_category': 1,
        }
        self.client.login(username='test_admin@food.net', password='pass')
        resp = self.client.post(reverse('invite'), data=data, follow=True)
        self.assertRedirects(resp, reverse('home'), status_code=302,
                             target_status_code=200, msg_prefix='')

        expected = 'Invitation has been send to {}'.format(invited_email)
        self.assertContains(resp, expected, 1, 200)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject,
                         'You have been invitate to FoodNet!')

        invitation = Invitation.objects.get(email=invited_email)
        url = absolute_url_reverse(
            'accept_invitation',
            kwargs=dict(verification_key=invitation.verification_key.hex)
        )
        self.assertRegex(invitation.verification_key.hex, r'^[a-z0-9]{32}\Z')
        self.assertIn(url, mail.outbox[0].body)

    def test_accept_invitation_flow(self):
        invited_email = 'test2@food.net'
        invitation = Invitation.objects.create(
                    email=invited_email,
                    invited_by=self.user,
                    department_id=1,
                    member_category_id=1)

        accept_invitation_url = reverse(
            'accept_invitation',
            kwargs=dict(verification_key=invitation.verification_key.hex)
        )

        if settings.USE_RECAPTCHA:
            resp = self.client.get(accept_invitation_url)
            self.assertContains(resp, 'accept invitation', 2)
            self.assertContains(resp, invitation.verification_key.hex, 1)

            data = {
                'recaptcha_response_field': 'PASSED',
            }
            resp = self.client.post(
                accept_invitation_url,
                data=data,
                follow=True
            )
            self.assertRedirects(resp, reverse('new_member_set_password'),
                                 status_code=302,
                                 target_status_code=200,
                                 msg_prefix='', )
        else:
            resp = self.client.get(accept_invitation_url, follow=True)
            self.assertRedirects(
                resp,
                reverse('new_member_set_password'),
                status_code=302,
                target_status_code=200
            )
        self.assertContains(resp, 'password1', 3)
        self.assertContains(resp, 'password2', 3)

        data = {
            'password1': 'passpass123',
            'password2': 'passpass123',
        }
        resp = self.client.post(
            reverse('new_member_set_password'),
            data=data,
            follow=True
        )
        self.assertRedirects(
            resp,
            reverse('account_login') + '?next=/membership/profile/',
            status_code=302,
            target_status_code=200
        )

        data = {
            'login': invited_email,
            'password': 'passpass123',
        }
        resp = self.client.post(
            reverse('account_login'),
            data=data,
            follow=True
        )
        self.assertRedirects(
            resp,
            reverse('profile'),
            status_code=302,
            target_status_code=200
        )

        # check if a new user is forced to complete it's profile
        resp = self.client.get(reverse('home'), follow=True)
        self.assertRedirects(
            resp,
            reverse('profile'),
            status_code=302,
            target_status_code=200
        )
        expected = 'Please update your profile.'
        actual = [m.message for m in list(resp.context['messages'])]
        self.assertIn(expected, actual)

        data = {
            'first_name': 'first_name',
            'middle_name': '',
            'last_name': 'last_name',
            'address': 'Vestergade 20C',
            'city': 'Copenhagen',
            'postcode': '123321',
            'tel': '231321321',
            'sex': UserProfile.FEMALE,
            'date_of_birth': '1980-01-01',
            'privacy': '1',
        }
        resp = self.client.post(reverse('profile'), data=data, follow=True)
        self.assertRedirects(
            resp,
            reverse('home'),
            status_code=302,
            target_status_code=200
        )
        expected = 'Your profile has been successfully updated.'
        actual = [m.message for m in list(resp.context['messages'])]
        self.assertIn(expected, actual)
        self.assertContains(resp, 'Log out', 1)
