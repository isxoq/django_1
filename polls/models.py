from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
