from django.db import models
from accounts.models import User


class Memory(models.Model):

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=250, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (str(self.id), self.title)
