from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.
from rest_framework import generics,status
from survey.models import Question, Survey
from .serializer import QuestionSerializer

'''
class ApiView(generics.ListAPIView):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer
 '''
 
@api_view(['GET','POST'])
def getQuiz(request):
  if request.method == 'GET':
    q = Question.objects.all()
    # op = Option.objects.all()
    qs = QuestionSerializer(q, many=True).data
    # ops = OptionSerializer(op, many = True).data
    data = qs
    return Response(data)
    

  elif request.method == 'POST':
    print(request.data)
    s = QuestionSerializer(data = request.data)
    print(s)
    if s.is_valid():
      print('success')
      s.save()
      return JsonResponse({'message': 'Data successfully saved!'})
    else:
      return JsonResponse({'message': s.is_valid()})
    
from django.core.serializers import serialize
import json
@api_view(['GET'])  
def survey_view(request):
  r = 'county'
  qs = Question.objects.raw("SELECT * FROM surveys_question WHERE survey_id_id=100")
  qs = serialize('json',qs)
  qs = json.loads(qs)
  return Response(qs)

