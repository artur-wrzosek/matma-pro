from django.db import models
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.utils.translation import gettext_lazy as _

class CreatedMixin:
    created_at = models.DateTimeField(auto_created=True)

class BaseUser(CreatedMixin, AbstractUser):
    created_by = models.ManyToManyField("self")
    phone = models.PositiveIntegerField(unique=True, default=123456789)
    phone_prefix = models.CharField(max_length=4, default="+48")


class BaseModel(CreatedMixin, models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_by = models.ForeignKey(BaseUser, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True

class School(BaseModel):
    class SchoolType(models.TextChoices):
        PRE = "preschool", _("Przedszkole")
        PRIMARY = "primary", _("Szkoła Podstawowa")
        HIGH = "high", _("Liceum")
        TECH = "tech", _("Technikum")
        COLLEGE = "college", _("Uczelnia Wyższa")

    type = models.CharField(max_length=30, choices=SchoolType, blank=True)

class Student(BaseUser):
    grade = models.PositiveSmallIntegerField()
    school = models.ManyToManyField(School, related_name="students")

class Parent(BaseUser):
    student = models.ManyToManyField(Student)

class Subject(BaseModel):
    pass


class Payment(BaseModel):
    class Method(models.TextChoices):
        stripe = "stripe", _("Stripe")
        cash = "cash", _("Gotówka")
        revolut = "revolut", _("Revolut")

    is_paid = models.BooleanField(default=False)
    payment_dt = models.DateTimeField(null=True)
    payer = models.ManyToManyField(Parent, related_name="payments")
    method = models.CharField(choices=Method.choices, max_length=30)



class Event(models.Model):
    event_dt = models.DateTimeField()
    online_url = models.URLField(null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    extended_level = models.BooleanField(default=False)
    payment = models.OneToOneField(Payment, on_delete=models.SET_NULL, null=True)
    notes = models.TextField(blank=True)
    was_rescheduled = models.BooleanField(default=False)
