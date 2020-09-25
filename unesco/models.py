from django.db import models

# Create your models here.
'''
class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    description = models.TextField(blank = True, null=True)
    justification = models.TextField(blank = True, null=True)
    longitude = models.DecimalField(max_digits=19, decimal_places=10,default =None, blank = True, null=True)
    latitude=models.DecimalField(max_digits=19, decimal_places=10,default =None, blank = True, null=True)
    area_hectares = models.IntegerField(null=True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self) :
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name


class Iso(models.Model) :
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name
'''

class States(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(max_length=200)
    justification=models.TextField(default="")
    year=models.IntegerField(default=0)
    latitude=models.FloatField(null=True,blank=True)
    longitude=models.FloatField(null=True,blank=True)
    area_hectares=models.FloatField(null=True,blank=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    iso=models.ForeignKey('Iso',on_delete=models.CASCADE,null=True)
    region=models.ForeignKey('Region',on_delete=models.CASCADE,null=True)
    states=models.ForeignKey('States',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
