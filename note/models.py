from django.db import models
from django.contrib.auth.models import User


class Importance(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    importance = models.ForeignKey(Importance, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.user) + " | " + self.title

    class Meta:
        ordering = ["-time_updated"]
