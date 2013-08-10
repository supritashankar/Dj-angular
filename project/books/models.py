from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    """ A simple model to store the details of the book """

    name              = models.CharField(max_length=70)
    author            = models.ForeignKey(User)
    publisher         = models.CharField(max_length=80)
    no_of_copies_sold = models.IntegerField(null=True, help_text="optional")

    def __unicode__(self):
        return u'{0} author being {1} publisher {2}'.format(self.name, self.author, self.publisher)
