from django.db import models
from django.contrib.auth import models as auth_models


class UserRestrictedModel(models.Model):
    field = models.CharField(max_length=100)
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
