from rest_framework import serializers

from main.models import (
    Quize,
    Constant,
    User, 
    UserQuize, 
    UserAnswer, 
    LevelUser, 
    AccesUser, 
    # QuizeAnswer, 
    # QuizeQuestion, 
    # QuizeTrueAnswer, 
    # StatusQuize
)

class QuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quize
        fields = ('id', 'quize_name', 'quize_description')


class ConstantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Constant
        fields = ('id', 'constant_name', 'constant_value')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'id_user_tg', 'user_login', 'user_full_name', 'user_level', 'user_access')


class UserQuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserQuize
        fields = ('id', 'id_user_tg', 'id_quize', 'quize_status', 'question_number', 'id_answer_last', 'quize_score')


class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ('id')


class LevelUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelUser
        fields = ('id')


class AccesUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccesUser
        fields = ('id')
