from rest_framework import serializers
from .models import  Question, QuestionType,QuestionOption
from ..WordPhrases.serializers import WordPhraseSerializer


class QuestionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionType
        fields = "__all__"

class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):

    question_type= QuestionTypeSerializer(read_only=True)
    options = QuestionOptionSerializer(many=True, read_only=True) 
    class Meta:
        model = Question
        fields = ["id","lesson","question_type","text","options"]

