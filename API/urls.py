from django.urls import path
from . import views

urlpatterns = [
  path('', views.getQuiz) ,
  path('/tag',views.survey_view) 
  ]