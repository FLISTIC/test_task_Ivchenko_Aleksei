from rest_framework import serializers

from .models import Inquirer,Questions,Answers,UserAnswers, UserInquirer,Users

class InquirerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquirer

        fields = (
            "id",
            "title",
            "date_start",
            "date_finish",
            "description",
        )

class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questions
        fields = (
            "id",
            "name",
            "type",
            "inquirer",
        )

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = (
            "id",
            "name",
            "questions",
        )

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "id",
            "name",
        )

class UserAnswersSerializer(serializers.ModelSerializer):
    answer = AnswersSerializer(many=True)
    class Meta:
        model = UserAnswers
        fields = (
            "user",
            "answer",
        )   

class UserInquirersSerializer(serializers.ModelSerializer):
    inquirer = InquirerSerializer(many=True)
    class Meta:
        model = UserInquirer
        fields = (
            "user",
            "inquirer",
        )       