from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    JOB_TYPE = {
        ('Full-Time','Full-Time'),
        ('Pull-Time','Pull-Time'),
    }
    owner = models.ForeignKey(User,on_delete=models.PROTECT)
    title = models.CharField(max_length=250)
    #location
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(max_length=250)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(max_length=250)
    active = models.BooleanField(default=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title
    



class Apply(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
