from django.db import models

# Create your models here.
class Titanic(models.Model):
    def __str__(self):
        return self.pclass
    age = models.IntegerField(default=0)
    fare = models.FloatField(default=0.0)
    sex = models.IntegerField(default=0)
    isalone = models.IntegerField(default=0)
    pclass = models.IntegerField(default=0)
    embarked = models.IntegerField(default=0)
    title = models.IntegerField(default=0)
