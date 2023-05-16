from rest_framework import serializers
from surveys.models import  Question, Survey, Response


# class OptionSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Option
#     fields = ('q_id', 'opt1', 'opt2', 'opt3', 'opt4')
    
class SurveySerializer(serializers.ModelSerializer):
  class Meta:
    model = Survey
    fields = ('survey_id', 'date_posted', 'survey_name')
    
    
class Response(serializers.ModelSerializer):
  class Meta:
    model = Response
    fields = ('q_tag', 'survey_id', 'response')
    
    
class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question 
    fields = ('q_id', 'q_no', 'quiz', 'survey_id','options','q_tag')