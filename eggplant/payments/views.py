import logging

from django.contrib import messages
from django.utils.translation import ugettext as _
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from getpaid.forms import PaymentMethodForm

from eggplant.common.views import LoginRequiredMixinView
from .models import Order
from .models import FeeConfig
from eggplant.membership.utils import is_account_owner
from eggplant.membership.models.account import Account

log = logging.getLogger(__name__)


@login_required
def payments_home(request):
    ctx = {
    }
    return render(request, 'eggplant/payments/payments_home.html', ctx)


@login_required
def fees_list(request):
    fees = FeeConfig.objects.all()
    ctx = {
        'fees': fees
    }
    return render(request, 'eggplant/payments/fees_list.html', ctx)


@login_required
def orders_list(request):
    orders = Order.objects.filter(account__user_profile__user=request.user).order_by('-created')
    ctx = {
        'orders': orders
    }
    return render(request, 'eggplant/payments/orders_list.html', ctx)


@login_required
def create_order_for_fee(request, fee_id):
    fee = get_object_or_404(FeeConfig, id=fee_id)
    account = Account.objects.get(user_profile__user=request.user)
    order = Order.objects.create_for_fee(account, fee)
    if not is_account_owner(request.user, account):
        raise PermissionDenied()
    return redirect('eggplant:payments:order_detail', pk=str(order.id))


class OrderView(LoginRequiredMixinView, DetailView):
    model = Order

    def get_template_names(self):
        return ['eggplant/payments/order_detail.html', ]

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['payment_form'] = PaymentMethodForm(
            self.object.currency,
            initial={'order': self.object}
        )
        return context

    @method_decorator
    @login_required
    def dispatch(self, request, *args, **kwargs):
        account = Account.objects.get(user_profile__user=request.user)
        if not is_account_owner(request.user, account):
            raise PermissionDenied()
        return super(OrderView, self).dispatch(request, *args, **kwargs)

order_detail = OrderView.as_view()


@login_required
def payment_accepted(request, pk=None):
    account = Account.objects.get(user_profile__user=request.user)
    if not is_account_owner(request.user, account):
        raise PermissionDenied()
    __ = get_object_or_404(Order, pk=pk)
    messages.info(request, _("Your payment has been accepted and"
                             " it's being processed."))
    return redirect('eggplant:payments:orders_list')


@login_required
def payment_rejected(request, pk=None):
    account = Account.objects.get(user_profile__user=request.user)
    if not is_account_owner(request.user, account):
        raise PermissionDenied()
    __ = get_object_or_404(Order, pk=pk)
    messages.error(request, _("Your payment has been cancelled."))
    return redirect("eggplant:payments:orders_list")
