from django.db import models


class M1Question(models.Model):

    M1QBNum = models.IntegerField(default=0)
    M1QSNum = models.IntegerField(default=0)
    M1QD = models.CharField(max_length=100)
    M1Q = models.CharField(max_length=100)
    One = models.BooleanField(default=False)
    Two = models.BooleanField(default=False)
    Three = models.BooleanField(default=False)
    Four = models.BooleanField(default=False)
    Five = models.BooleanField(default=False)



    def __int__(self):
        return self.M1QBNum


class M1Answer(models.Model):

    m1question = models.ForeignKey(M1Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


# Create your models here.
