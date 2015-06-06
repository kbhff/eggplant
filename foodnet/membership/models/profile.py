from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )

    user = models.OneToOneField('auth.User', editable=False)
    middle_name = models.CharField(max_length=30, null=True)

    # old system: adr1, adr2, streetno, floor, door
    address = models.TextField(max_length=255)
    postcode = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    tel2 = models.CharField(max_length=15, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    date_of_birth = models.DateField(null=True)  # old system: birthday
    privacy = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    changed = models.DateTimeField(auto_now=True, editable=False)
    account = models.ManyToManyField(
        'membership.Account',
        through='membership.AccountMembership'
    )

    def __str__(self):
        return 'Profile({0})'.format(self.user)

    @property
    def full_name(self):
        "Returns member's full name."
        if self.middlename:
            return '{0} {1} {2}'.format(self.user.firstname, self.middlename,
                                        self.user.lastname)
        return '{0} {2}'.format(self.user.firstname, self.user.lastname)

    def is_complete(self):
        if self.address and self.postcode and self.city and \
                self.sex and self.tel and self.date_of_birth and self.privacy:
            return True
        return False

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.get(user_id=user.id)


@receiver(post_save, sender=User, dispatch_uid='membership-user-profile')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
