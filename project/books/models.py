from django.db import models

# Create your models here.

class Books(models.Model):
    """ A simple model to store the details of the book """

    name              = models.CharField(max_length=70)
    author            = models.CharField(max_length=70)
    publisher         = models.CharField(max_length=80)
    no_of_copies_sold = models.IntegerField(null=True, help_text="optional")
