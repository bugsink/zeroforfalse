from django.db import models


class MyModel(models.Model):
    boolean_field = models.BooleanField(default=False)
