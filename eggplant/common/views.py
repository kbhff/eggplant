from django.contrib.auth.decorators import login_required


class LoginRequiredMixinView(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixinView, cls).as_view(**kwargs)
        return login_required(view)
