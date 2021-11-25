from django.db import models

# Create your models here.
class features(models.Model):
    name:models.CharField(max_length=55)
    details:models.CharField(max_length=555)