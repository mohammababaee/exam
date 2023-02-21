from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=250)

class Answer(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=50,blank=False,null= False)
    is_correct = models.BooleanField(default=False)

class UserChoice(models.Model):
    answer = models.OneToOneField(Answer, related_name="choices")
    submited = models.BooleanField(default=False)