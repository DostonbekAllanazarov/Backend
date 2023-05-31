from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.TextField()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    theme = models.CharField(max_length=500)

    def __str__(self):
        return self.theme

class Answers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)   
    answer = models.CharField(max_length=500)

    def __str__(self):
        return self.answer