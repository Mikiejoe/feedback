from django.urls import path
from .views import getQuiz

urlpatterns = [
  path('', getQuiz) , 
  ]