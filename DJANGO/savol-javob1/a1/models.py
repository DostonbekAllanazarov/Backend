from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='media/profile_images/')

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    #created_time = models.DateTimeField(auto_now_add=True)
    #updated_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.question

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.answer