from django.db import models

# Create your models here.

class Transport(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    numb= models.CharField(max_length=10, null=False, unique=True)
    def __str__(self):
        return f'{self.name}, {self.numb}'

    def most_recent(self):
        return self.report.latest('created')

class Report(models.Model):
    car= models.ForeignKey(
        Transport,
        related_name='report',
        on_delete=models.SET_NULL,
        null=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(null=False)
    cons= models.FloatField(null=True)
