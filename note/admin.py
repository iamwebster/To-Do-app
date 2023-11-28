from django.contrib import admin
from .models import Task, Importance


admin.site.register(Task)
admin.site.register(Importance)