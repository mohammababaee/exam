from users_exam import Exams
from django.db import models
from django.contrib.auth.models import User


class UserProfle(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    exams = models.ForeignKey(Exams,on_delete=models.CASCADE)