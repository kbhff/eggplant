# coding: utf8
import uuid

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from allauth.account.models import EmailAddress

from eggplant.membership.models import UserProfile
from eggplant.membership.factories import (
    UserFactory,
    AccountFactory,
    DepartmentFactory,
)

from .models import Order, FeeConfig


class TestPayments(TestCase):

    def setUp(self):
        self.test_user = UserFactory()
        # FIXME: mock Userprofile.is_complete to return True
        UserProfile.objects.filter(user_id=self.test_user.id).update(
            address=' test address',
            postcode='test postcode',
            city='test city',
            sex='f',
            tel='test tel',
            date_of_birth=timezone.now(),
            privacy=True,
            user=self.test_user
        )
        self.test_user.set_password('pass')
        self.test_user.save()
        email_address = EmailAddress.objects\
            .add_email(None, self.test_user, 'test@eggplant.dk', confirm=False,
                       signup=False)
        email_address.verified = True
        email_address.primary = True
        email_address.save()

        department = DepartmentFactory()
        account = AccountFactory(department=department)
        account.accountmembership_set\
            .create(user_profile=self.test_user.profile, role='owner')

        self.client.login(email='test@eggplant.dk', password='pass')

    def test_payments_home(self):
        response = self.client.get(reverse('eggplant:payments:payments_home'))
        self.assertEqual(response.status_code, 200)

    def test_fees_list(self):
        response = self.client.get(reverse('eggplant:payments:fees_list'))
        self.assertEqual(response.status_code, 200)

    def test_orders_list(self):
        fee = FeeConfig.objects.get(name='membership')
        order = Order.objects.create_for_fee(self.test_user, fee)
        response = self.client.get(reverse('eggplant:payments:orders_list'))
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(list(response.context['orders']), [order, ])

    def test_order_detail(self):
        fee = FeeConfig.objects.get(name='membership')
        order = Order.objects.create_for_fee(self.test_user, fee)
        response = self.client.get(reverse('eggplant:payments:order_detail',
                                           kwargs=dict(pk=str(order.id))))
        self.assertEqual(response.status_code, 200)

    def test_create_order_for_fee(self):
        fee = FeeConfig.objects.get(name='membership')
        url = reverse('eggplant:payments:create_order_for_fee',
                      kwargs=dict(fee_id=fee.id))
        response = self.client.get(url)
        orders = Order.objects.filter(user=self.test_user)
        self.assertEqual(1, orders.count())
        order = orders[0]
        expected_url = reverse('eggplant:payments:order_detail',
                               kwargs=dict(pk=str(order.id)))
        self.assertRedirects(response, expected_url, 302, 200)

    def test_payment_accepted_nonexistent_order(self):
        non_existent = uuid.uuid4()
        response = self.client.get(
            reverse('eggplant:payments:payment_accepted',
                    kwargs=dict(pk=non_existent)))
        self.assertEqual(response.status_code, 404)

    def test_payment_accepted(self):
        fee = FeeConfig.objects.get(name='membership')
        order = Order.objects.create_for_fee(self.test_user, fee)
        response = self.client.get(
            reverse('eggplant:payments:payment_accepted',
                    kwargs=dict(pk=str(order.id))), follow=True)

        expected_url = reverse('eggplant:payments:orders_list')
        self.assertRedirects(response, expected_url, 302, 200,
                             fetch_redirect_response=True)

        expected = ("Your payment has been accepted and"
                    " it's being processed.")
        msgs = [m.message for m in list(response.context['messages'])]
        self.assertEqual(1, len(msgs))
        self.assertIn(expected, msgs)

    def test_payment_rejected_nonexistent_order(self):
        non_existent = uuid.uuid4()
        response = self.client.get(
            reverse('eggplant:payments:payment_rejected',
                    kwargs=dict(pk=non_existent)))
        self.assertEqual(response.status_code, 404)

    def test_payment_rejected(self):
        fee = FeeConfig.objects.get(name='membership')
        order = Order.objects.create_for_fee(self.test_user, fee)
        response = self.client.get(
            reverse('eggplant:payments:payment_rejected',
                    kwargs=dict(pk=str(order.id))), follow=True)
        expected_url = reverse('eggplant:payments:orders_list')
        self.assertRedirects(response, expected_url, 302, 200,
                             fetch_redirect_response=True)

        expected = ("Your payment has been cancelled.")
        msgs = [m.message for m in list(response.context['messages'])]
        self.assertEqual(1, len(msgs))
        self.assertIn(expected, msgs)
