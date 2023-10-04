import datetime

from django.db import models
from django.utils import timezone


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField("birthday date")
    next_treatment = models.DateTimeField("next treatment")

    def incoming_treatment(self):
        return self.next_treatment >= timezone.now() - datetime.timedelta(days=7)

    def incoming_birthday(self):
        return self.next_treatment >= timezone.now() - datetime.timedelta(days=7)
