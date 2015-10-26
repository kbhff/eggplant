from django.test import TestCase

# Create your tests here.
from eggplant.factories import DepartmentFactory, UserFactory, \
    DepartmentAdministratorFactory, AccountFactory, AccountMembershipFactory


class TestDeparmentAdmin(TestCase):

    def setUp(self):
        # create dept and admin user
        self.department = DepartmentFactory()
        self.admin_user = UserFactory()
        DepartmentAdministratorFactory(profile=self.admin_user.userprofile, department=self.department)

        # let's add some account/profiles
        account1 = AccountFactory(department=self.department)
        u1 = UserFactory()
        AccountMembershipFactory(account=account1, user_profile=u1.userprofile)
        # AccountMembershipFactory(account=account1)
        #

    def test_user_is_department_admin(self):
        profile = self.admin_user.userprofile
        self.assertTrue(profile.has_admin_permission(self.department),
                        "User does not have admin permission on department")

    def test_admin_can_edit_dept_profiles(self):
        admin = self.admin_user.userprofile

        profiles = UserProfile.in_department(self.department)

        for profile in profiles:
            self.assertTrue(profile.can_be_edited_by(admin))

    def test_admin_cannot_edit_other_dept_profiles(self):
        admin = self.admin_user.userprofile

        other_dept = DepartmentFactory()
        AccountMembershipFactory(account=AccountFactory(department=other_dept),
                                 user_profile=UserFactory().userprofile)

        for profile in UserProfile.in_department(other_dept):
            self.assertFalse(profile.can_be_edited_by(admin))