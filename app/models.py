from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    username=models.CharField(max_length=20)
    desc=models.TextField()

    def __str__(self):
        return self.name