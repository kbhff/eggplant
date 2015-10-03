from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    MALE, FEMALE, OTHER = range(3)
    SEX_CHOICES = (
        ('', '-----'),
        (FEMALE, _('female')),
        (MALE, _('male')),
        (OTHER, _('other')),
    )

    permissions = models.ManyToManyField(
        "Permission",
        verbose_name=_("permissions"),
        blank=True
    )
    account = models.ForeignKey(
        'membership.Account',
        verbose_name=_("account"),
        null=True,
        related_name='profiles',
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        editable=False,
        related_name='profile',
        verbose_name=_("user"),
    )
    middle_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name=_("middle name"),
        help_text=_("Optional.")
    )

    # TODO: Why is this a TextField!?
    address = models.TextField(max_length=255)
    postcode = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15)
    sex = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES,
        null=True,
    )
    # TODO: Can we just remove this!?
    date_of_birth = models.DateField(null=True)  # old system: birthday
    # TODO: What does this mean???
    privacy = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    changed = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return 'Profile({0})'.format(self.user)

    @property
    def full_name(self):
        "Returns member's full name."
        if self.middle_name:
            return '{0} {1} {2}'.format(self.user.firstname, self.middle_name,
                                        self.user.lastname)
        return '{0} {2}'.format(self.user.firstname, self.user.lastname)

    def is_complete(self):
        return all([self.address, self.postcode, self.city, self.tel])


# TODO: This does not work with AUTH_USER_MODEL
# See: https://github.com/django/django/commit/fdb5c98d7ee54c7f89ec10b0203263f1f5b37510
# @receiver(post_save, sender=User, dispatch_uid='membership-user-profile')
# Instead, we create the user automatically through factories.
def create_user_profile(sender, instance, created, **kwargs):
    """Every time a user is created, we automatically create a profile for
    the user."""
    if created:
        # Set the reverse instance.profile so the new profile is available
        # immediately
        instance.profile = UserProfile.objects.create(user=instance)
