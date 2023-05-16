from django.db import models
# import jsonfield
import jsonfield

# Create your models here.
class Survey(models.Model):
  survey_id = models.CharField(max_length=50,primary_key=True)
  date_posted = models.DateField()
  survey_name = models.CharField(max_length=50)

  def __str__(self):
    return self.survey_name
  
class Question(models.Model):
  q_id = models.CharField(max_length = 50,primary_key=50)
  q_no = models.IntegerField()
  quiz = models.CharField(max_length=250)
  q_tag = models.CharField(max_length=50 , unique=True,null=True)
  survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
  options = jsonfield.JSONField()
  
  def __str__(self):
    return self.quiz
  
# class Option(models.Model):
#   q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
#   opt1 = models.CharField(max_length=50)
#   opt2 = models.CharField(max_length=50)
#   opt3 = models.CharField(max_length=50)
#   opt4 = models.CharField(max_length=50)

  
  
class Response(models.Model):
  q_tag = models.ForeignKey(Question, on_delete=models.CASCADE, to_field='q_tag')

  survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
  response = models.CharField(max_length=50)