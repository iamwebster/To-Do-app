from django.contrib import admin
from .models import Task, Importance
from django.contrib.auth.models import Group


admin.site.register(Task)
admin.site.register(Importance)

admin.site.unregister(Group)