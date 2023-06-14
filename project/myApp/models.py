from django.db import models

# Create your models here.

class President(models.Model):
    class Sex(models.TextChoices):
        MALE = 'm'
        FEMALE = 'f'
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(choices=Sex.choices, max_length=1)
    img = models.ImageField(upload_to='myApp/img', blank=True)
    url_img = models.URLField(blank=True)
    def __str__(self):
        return (self.name)
    
class Country(models.Model):
    president = models.OneToOneField(President, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    population = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=50)
    def __str__(self):
        return (self.name)

class Project(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return (self.name)

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return (self.name)

