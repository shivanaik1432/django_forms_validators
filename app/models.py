from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    mail=models.CharField(max_length=100)
    remail=models.CharField(max_length=100)
    number=models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)
