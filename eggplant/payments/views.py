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
from eggplant.membership.utils import is_account_owner
from eggplant.membership.models.account import Account
from .models import Payment

log = logging.getLogger(__name__)


@login_required
def payments_home(request):
    return redirect('eggplant:payments:payment_list')


@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user).payment_by('-created')
    ctx = {
        'payments': payments
    }
    return render(request, 'eggplant/payments/payment_list.html', ctx)


@login_required
def payment_info(request, pk=None):
    payment = get_object_or_404(Payment, pk=pk, user=request.user)
    ctx = {
        'payments': [payment, ]
    }
    return render(request, 'eggplant/payments/payment_list.html', ctx)


class PaymentView(LoginRequiredMixinView, DetailView):
    model = Payment
    template_name = 'eggplant/payments/payment_detail.html'

    @method_decorator
    @login_required
    def dispatch(self, request, *args, **kwargs):
        account = Account.objects.get(user_profile__user=request.user)
        if not is_account_owner(request.user, account):
            raise PermissionDenied()
        return super(PaymentView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Payment.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        context['payment_form'] = PaymentMethodForm(
            self.object.currency,
            initial={'payment': self.object}
        )
        return context

payment_detail = PaymentView.as_view()


@login_required
def payment_accepted(request, pk=None):
    account = Account.objects.get(user_profile__user=request.user)
    if not is_account_owner(request.user, account):
        raise PermissionDenied()
    __ = get_object_or_404(Payment, pk=pk, user=request.user)
    messages.info(request, _("Your payment has been accepted and"
                             " it's being processed."))
    return redirect('eggplant:payments:payments_list')


@login_required
def payment_rejected(request, pk=None):
    account = Account.objects.get(user_profile__user=request.user)
    if not is_account_owner(request.user, account):
        raise PermissionDenied()
    __ = get_object_or_404(Payment, pk=pk, user=request.user)
    messages.error(request, _("Your payment has been cancelled."))
    return redirect("eggplant:payments:payments_list")
