from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=10, unique=True)
    profile_photo = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name