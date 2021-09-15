import json
from django.db.models import query
from django.shortcuts import render
import datetime
from django.http import Http404
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from django.conf import settings

from .models import Inquirer,Questions,Answers,UserAnswers, UserInquirer,Users
from rest_framework.viewsets import ModelViewSet


from .serializers import AnswersSerializer, InquirerSerializer, QuestionsSerializer, UserAnswersSerializer, UserInquirersSerializer, UsersSerializer

class InquirerViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Inquirer.objects.all()
    serializer_class = InquirerSerializer

    # def get(self, request, format=None):

    #     inquirer = Inquirer.objects.all()
        
    #     serializer = InquirerSerializer(inquirer, many=True)
    #     return Response(serializer.data)


class QuestionsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class UserAnswerViewSet(ModelViewSet):
    queryset = UserAnswers.objects.all()
    serializer_class = UserAnswersSerializer

class AnswerViewSet(ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

class UserInquirerViewSet(ModelViewSet):
    queryset = UserInquirer.objects.all()
    serializer_class = UserInquirersSerializer

@api_view(['GET'])
def get_active_inquirers(request):
    inquirers = Inquirer.objects.filter(date_finish__gt=datetime.datetime.now())
    serialized = InquirerSerializer(inquirers,many=True)
    return Response(serialized.data)

@api_view(['GET'])
def question_list(request,id):

    questions = Questions.objects.filter(inquirer=Inquirer.objects.get(id=id))
    
    serializer = QuestionsSerializer(questions, many=True)

    return Response(serializer.data)  

# @api_view(['POST'])
# def put_answers(request, id):
    
#     print(answers)
#     user = Users.objects.get(id=id)
#     for answer in answers:
#         print(answer)
#         UserAnswers.objects.create(user=user, answer = Answers.objects.create(**answer))
#     return Response('OK')
# 
# @api_view(['POST'])
# def contractAdd(request):
#     print(request.body)
#     data=json.loads(request.body)
#     print(request.user)
#     for data_ in data:
#         newAnswer=Answers(questions=Questions.objects.get(id=data['id']),name=data['name'],address=data['address'],slug=data['slug'],description=data['description'],price=data['price'],image=data['image'],thumbnail=data['thumbnail'],
#                                 id_create=request.user
#                             )
#     newAnswer.save()
#     return Response( status=status.HTTP_201_CREATED)     