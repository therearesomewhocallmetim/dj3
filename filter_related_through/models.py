from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=500)


class Profession(models.Model):
    name = models.CharField(max_length=500)
    users = models.ManyToManyField(User, through='UserProfession')


class UserProfession(models.Model):
    user = models.ForeignKey(
        User, related_name="professions", on_delete=models.CASCADE, db_index=True
    )
    profession = models.ForeignKey(Profession, blank=True, null=True, on_delete=models.CASCADE)
    period = DateTimeRangeField()
