from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name



class Cancer(models.Model):
    NPFFR1 = models.CharField(max_length=100)
    TAS2R19 = models.CharField(max_length=100)
    ADRA2C = models.CharField(max_length=100)
    SOWAHA = models.CharField(max_length=100)
    TAS2R60 = models.CharField(max_length=100)
    KRT20 = models.CharField(max_length=100)
    AADACL4 = models.CharField(max_length=100)
    NACA2 = models.CharField(max_length=100)
    CLDN8 = models.CharField(max_length=100)
    GJC3 = models.CharField(max_length=100)
    FEM1A = models.CharField(max_length=100)
    DRD5 = models.CharField(max_length=100)
    PABPC3 = models.CharField(max_length=100)
    HIST1H4C = models.CharField(max_length=100)
    MC2R = models.CharField(max_length=100)

    def __str__(self):
        return self.NPFFR1



class visualise(models.Model):
    Cancer_Class = models.CharField(max_length=100)
    image = models.FileField(null=True,blank=True)
    Description = models.TextField()
    Symptoms = models.TextField()

    def __str__(self):
        return self.Cancer_Class



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title