from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=20)
    volume = models.IntegerField()
    proof = models.IntegerField()

    def alcohol(self):
        return self.volume / 100 * self.proof
