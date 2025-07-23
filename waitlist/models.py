from django.db import models

# Create your models here.
class Waitlist(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f" {self.name} - {self.email}"