from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.name, self.code)

class Professional(models.Model):
    OPTION_IDENTIFICATION = (
        ('dni', 'dni'),
        ('le','le'),
        ('lc','lc'),
    )
    person = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cuil = models.CharField(max_length=30, null=True)
    identification = models.CharField(choices=OPTION_IDENTIFICATION, max_length=4, null=True)
    code_identification = models.CharField(max_length=50, null=True, blank=True)
    related_skill = models.ManyToManyField('Skill', blank=True)
    born_date = models.DateField(null=True, default=timezone.now)
    def get_related_skill(self):
        if self.related_skill is not None and self.related_skill:
            return self.related_skill.all()

    def __str__(self):
        return '%s. %s, %s' % (self.person.first_name, self.person.last_name, self.code_identification)