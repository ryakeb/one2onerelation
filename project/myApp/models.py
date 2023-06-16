from django.db import models

# Create your models here.
### EXO 1 ### 
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

### EXO 2 ###

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

### EXO 3 ###

class Question(models.Model):
    class Category(models.TextChoices):
        SPORT = 'sport'
        HISTORY = 'history'
        SCIENCES = 'sciences'
        GEOGRAPHY = 'geography'
        MUSIC = 'music'
        CINEMA = 'cinema'
        FUNFACTS = 'fun facts'
    question_text = models.CharField(max_length=300)
    category = models.CharField(choices=Category.choices, max_length=20)
    def __str__(self):
        return (self.question_text)

class Answer(models.Model):
    answer_text = models.CharField(max_length=300)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    