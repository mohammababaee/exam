from django.db import models
from user import UserProfle
from question import Question
# Create your models here.

class Exam(models.Model):
    user = models.ForeignKey(UserProfle,on_delete=models.CASCADE)
    score = models.IntegerField()
    is_passed = models.BooleanField()
    questions = models.ForeignKey(Question,on_delete=models.CASCADE)