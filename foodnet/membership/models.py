# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )
    
    user = models.OneToOneField(User)
    middlename = models.CharField(max_length=255)
    adr1 = models.CharField(max_length=255)
    adr2 = models.CharField(max_length=255)
    streetno = models.CharField(max_length=255)
    floor = models.CharField(max_length=255)
    door = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    tel2 = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(null=True)
    privacy = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    def _get_full_name(self):
        "Returns member's full name."
        return '{0} {1} {2}'.format(self.user.firstname, self.middlename,
                                    self.user.lastname)
    full_name = property(_get_full_name)


class Member(models.Model):
    number = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User)


class Division(models.Model):
    shortname = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    webmembers = models.BooleanField()  # FIXME: should this be here?
    contact = models.CharField(max_length=255)


class DivisionMembers(models.Model):
    member = models.ForeignKey(Member)
    division = models.ForeignKey(Division)
    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = (('member', 'division'),)
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
