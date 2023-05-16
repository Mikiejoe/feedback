from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from surveys.models import Question, Survey
from .serializer import QuestionSerializer

'''
class ApiView(generics.ListAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
 '''
 
@api_view()
def getQuiz(request):
  if request.method == 'GET':
    q = Question.objects.all()
    # op = Option.objects.all()
    qs = QuestionSerializer(q, many=True).data
    # ops = OptionSerializer(op, many = True).data
    data = qs
    return Response(data)
    