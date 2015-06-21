from django import template
from eggplant.membership import utils

register = template.Library()


@register.filter
def is_active_account_owner(user):
    return utils.is_active_account_owner(user)
