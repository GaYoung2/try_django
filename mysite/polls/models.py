import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):  #table
    question_text = models.CharField(max_length=200) #models에서 charField도 class name
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200) #선택문항
    votes = models.IntegerField(default=0)  #설문의 선택문항에 응답한 사람이 몇명

    def __str__(self):
        return self.choice_text