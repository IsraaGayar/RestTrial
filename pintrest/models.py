from django.db import models

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=225,verbose_name='review name')
    comment = models.TextField(default='movie def', null=True,blank=True)
    creationDate = models.DateField(auto_now_add=True)


class Actor(models.Model):
    name = models.CharField(max_length=225,verbose_name='actor name')
    biography = models.TextField(default='movie def', null=True,blank=True)
    age = models.IntegerField(blank=True, null=True)
    Birthdate = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField(default='movie def', null=True)
    likes = models.IntegerField(default=0, null=True)
    watchCount = models.IntegerField(default=0, null=True)
    rate = models.PositiveIntegerField(default=0, null=True)
    productionDate = models.DateField(null=True, blank=True)
    creationDate = models.DateField(auto_now_add=True)
    modificationDate = models.DateField(auto_now=True)
    actors = models.ManyToManyField('Actor',blank=True,null=True)

    def __str__(self):
        return self.name
