from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.pk)+' '+self.name
    
class Publication(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=9)
    authors = models.ManyToManyField('Authors', related_name='books')
    pubication = models.ForeignKey('Publication', related_name='books', on_delete=models.CASCADE)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    