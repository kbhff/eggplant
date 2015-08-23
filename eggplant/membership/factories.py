# coding: utf8
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
import factory


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: 'user%d@food.net' % n)
    userprofile = factory.RelatedFactory(
        'eggplant.membership.factories.UserProfileFactory',
        'user'
    )

    class Meta:
        model = 'auth.User'

    @classmethod
    def _generate(cls, create, attrs):
        """Override the default _generate() to disable the post-save signal."""
        from eggplant.membership.models.profile import create_user_profile
        post_save.disconnect(create_user_profile, get_user_model(),
                             dispatch_uid='membership-user-profile')
        user = super(UserFactory, cls)._generate(create, attrs)
        post_save.connect(create_user_profile, get_user_model(),
                          dispatch_uid='membership-user-profile')
        return user


class UserProfileFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'membership.UserProfile'

    user = factory.SubFactory('eggplant.membership.factories.UserFactory',
                              userprofile=None)


class AccountFactory(factory.DjangoModelFactory):
    department = factory.SubFactory(
        'eggplant.membership.factories.DepartmentFactory'
    )
    category = factory.SubFactory(
        'eggplant.membership.factories.AccountCategoryFactory'
    )

    class Meta:
        model = 'membership.Account'


class AccountCategoryFactory(factory.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'category%d' % n)

    class Meta:
        model = 'membership.AccountCategory'


class AccountMembershipFactory(factory.DjangoModelFactory):
    user_profile = factory.SubFactory('foodnet.membership.factories.UserProfileFactory')
    account = factory.SubFactory('foodnet.membership.factories.AccountFactory')

    class Meta:
        model = 'membership.AccountMembership'


class DepartmentFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'membership.Department'


class DepartmentAdministratorFactory(factory.DjangoModelFactory):
    profile = factory.SubFactory('foodnet.membership.factories.UserProfileFactory')
    department = factory.SubFactory('foodnet.membership.factories.DepartmentFactory')

    class Meta:
        model = 'membership.DepartmentAdministrator'


class DepartmentInvitationFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'membership.DepartmentInvitation'
