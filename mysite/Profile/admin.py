from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Professional, Skill

admin.site.register(Professional)
admin.site.register(Skill)
