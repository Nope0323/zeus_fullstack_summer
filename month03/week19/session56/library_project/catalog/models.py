from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharFeild(max_legth=200, verbosa_name="Book name")
    author_name = models.CharField(max_length=200, verbose_name="Author Name")
    published_date = models.DateFeild(verbose_name="published Date")
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN Number" )

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    birth_date = models.DateField(verbose_name="Birthday")
    biography = models.TextField(blank=True, null=True, verbosa_name="Biography")

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField()
    email = models.EmailField()
    join_date = models.DateField()