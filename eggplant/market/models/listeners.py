"""
Notice: getpaid calls it "order" objects, however since our payments app does
not model orders, we also call this "payment" in eggplant.payments.models
"""

import logging

from django.forms import ValidationError
from getpaid import signals

log = logging.getLogger(__name__)


def new_payment_query_listener(sender, order=None, payment=None, **kwargs):
    """
    Fills in required payment details.
    """
    payment.amount = order.amount.amount
    payment.currency = order.amount.currency
signals.new_payment_query.connect(new_payment_query_listener)


def user_data_query_listener(sender, order=None, user_data=None, **kwargs):
    """
    Fills in required user details.
    """
    user_data['email'] = ''
signals.user_data_query.connect(user_data_query_listener)


def payment_status_changed_listener(sender, instance, old_status, new_status,
                                    **kwargs):
    """
    Here we will actually do something, when payment is accepted.
    E.g. lets change an order status based on payment status.
    """
    if old_status != 'paid' and new_status == 'paid':
        # Ensures that we process order only once
        log.debug("payment for order %s has changed status to %s",
                  instance.order.id, instance.status)
signals.payment_status_changed.connect(payment_status_changed_listener)


def new_payment_listener(sender, order=None, payment=None, **kwargs):
    """
    Log how many and which payments were made.
    """
    log.debug("order %s: payment: %s", order.__dict__, payment.__dict__)
signals.new_payment.connect(new_payment_listener)


def order_additional_validation_listener(sender, request=None, order=None,
                                         backend=None, **kwargs):
    """
    Custom validation.
    """
    log.debug("%s order %s: backend: %s",
              request.user, order.__dict__, backend)
    if request.user != order.user:
        raise ValidationError("user is not owner of the order")
signals.order_additional_validation.connect(
    order_additional_validation_listener)
