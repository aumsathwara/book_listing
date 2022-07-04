from django.db import models
from django.forms import CharField

# Create your models here.

class Book_List(models.Model):
    Db_Name = models.CharField(max_length=200)

    def __str__(self):
        return self.Db_Name


class Book_Item(models.Model):
    key = models.ForeignKey(Book_List, on_delete=models.CASCADE)
    booktitle = models.CharField(max_length=500)
    cart_boolean = models.BooleanField()
    count = models.IntegerField(default=0)
    content = models.CharField(max_length=500, default="Shut up!")
    price = models.FloatField(default=0)
    image = models.CharField(max_length=500, default="nikal bc!")


    def __str__(self):
        return self.booktitle