from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_quiz, name='start_quiz'),
    path('question/<int:q_no>/', views.quiz_question, name='quiz_question'),
    path('result/', views.quiz_result, name='quiz_result'),
]
