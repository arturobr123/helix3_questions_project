from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .serializers import CommentSerializer
from .models import Question
from .models import Comment

# Create your views here.

class QuestionView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()