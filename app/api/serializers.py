from rest_framework import serializers

from main.models import (
    Quize,
    Constant,
    User,
    UserQuize,
    UserAnswer,
    LevelUser,
    AccesUser,
    QuizeAnswer,
    QuizeQuestion,
    QuizeTrueAnswer,
    StatusQuize,
)

class QuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quize
        fields: tuple[str] = (
            'id',
            'quize_name',
            'quize_description'
        )


class ConstantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Constant
        fields: tuple[str] = (
            'id', 
            'constant_name', 
            'constant_value'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields: tuple[str] = (
            'id', 
            'id_user_tg', 
            'user_login', 
            'user_full_name', 
            'user_level', 
            'user_access'
        )


class UserQuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserQuize
        fields: tuple[str] = (
            'id', 
            'id_user_tg', 
            'id_quize', 
            'quize_status', 
            'question_number', 
            'id_answer_last', 
            'quize_score'
        )


class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAnswer
        fields: tuple[str] = (
            'id', 
            'id_user_tg', 
            'id_user_quize', 
            'id_answer',
            'question_number'
        )


class LevelUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LevelUser
        fields: tuple[str] = (
            'id', 
            'level_text', 
            'min_level_score', 
            'max_level_score'
        )


class AccesUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccesUser
        fields: tuple[str] = (
            'id', 
            'acces_text'
        )


class QuizeAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizeAnswer
        fields: tuple[str] = (
            'id', 
            'id_quize', 
            'question_number', 
            'answer_number', 
            'answer_text'
        )


class QuizeQuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizeQuestion
        fields: tuple[str] = (
            'id',
            'id_quize',
            'question_number',
            'question_text'
        )


class QuizeTrueAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizeTrueAnswer
        fields: tuple[str] = (
            'id',
            'id_quize',
            'id_answer',
            'question_number',
        )


class StatusQuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StatusQuize
        fields: tuple[str] = (
            'id',
            'status_text'
        )
