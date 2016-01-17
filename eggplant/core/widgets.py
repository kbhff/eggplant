from djmoney.forms import widgets as money_widgets


class MoneyWidget(money_widgets.MoneyWidget):

    def __init__(self, *args, **kwargs):
        if 'attrs' not in kwargs:
            kwargs['attrs'] = {}
        # Use any class attr or default to money-widget
        kwargs['attrs']['class'] = kwargs['attrs'].get('class', 'money-widget')
        super(MoneyWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        result = '<div class="input-group">'
        result += super(MoneyWidget, self).render(name, value, attrs)
        result += '</div>'
        return result
