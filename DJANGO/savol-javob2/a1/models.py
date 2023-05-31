from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'profile_images', default="profile_images/profile.jpg")

class Question(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['-id']    
    

class Answer(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.answer
    class Meta:
        ordering = ['-id']    
    