from datetime import datetime

from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models
from django.db.models import Prefetch


class UserQuerySet(models.QuerySet):
    def with_professions(self):
        pref = Prefetch('professions', queryset=UserProfession.objects.current())
        return self.prefetch_related(pref)


class User(models.Model):
    name = models.CharField(max_length=500)

    objects = UserQuerySet.as_manager()


class Profession(models.Model):
    name = models.CharField(max_length=500)
    users = models.ManyToManyField(User, through='UserProfession')


class UserProfessionQuerySet(models.QuerySet):
    def current(self):
        return self.filter(period__contains=datetime.now()).select_related('profession')


class UserProfession(models.Model):
    user = models.ForeignKey(
        User,
        related_name="professions", on_delete=models.CASCADE, db_index=True)
    profession = models.ForeignKey(
        Profession, blank=True, null=True, on_delete=models.CASCADE)
    period = DateTimeRangeField()

    objects = UserProfessionQuerySet.as_manager()


def the_fn():
    rng = User.objects.with_professions().get(pk=1)
    print(f'ringo is a {[x.profession.name for x in rng.professions.all()]}')
