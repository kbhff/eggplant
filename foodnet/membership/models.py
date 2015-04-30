# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    MALE = 'm'
    FEMALE = 'f'
    SEX_CHOICES = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )
    
    user = models.OneToOneField(User)
    middlename = models.CharField(max_length=255)
    
    # old system: adr1, adr2, streetno, floor, door
    address = models.TextField(max_length=2000)
    postcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    tel2 = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(null=True)
    privacy = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        "Returns member's full name."
        return '{0} {1} {2}'.format(self.user.firstname, self.middlename,
                                    self.user.lastname)


class Member(models.Model):
    number = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User)


class Division(models.Model):
    shortname = models.CharField(max_length=4)
    name = models.CharField(max_length=255)
    
    # old system: type
    category = models.CharField(max_length=255)
    
    # old system: webmembers
    allow_webmembers = models.BooleanField()
    contact = models.CharField(max_length=255)

    # FIXME: should we move it out to model manager with
    # other bits from old models?
    #members = models.ManyToManyField('membership.Member',
    #                                 through='membership.DivisionMember')


class DivisionMember(models.Model):
    member = models.ForeignKey(Member)
    division = models.ForeignKey(Division)
    start = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField()
    active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = (('member', 'division'),)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
