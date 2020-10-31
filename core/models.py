from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
