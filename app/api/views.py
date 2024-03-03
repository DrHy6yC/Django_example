from rest_framework import viewsets

from api  import serializers


class QuizeViewSet(viewsets.ModelViewSet):
    queryset = serializers.Quize.objects.all().order_by('quize_name')
    serializer_class = serializers.QuizeSerializer

class ConstantViewSet(viewsets.ModelViewSet):
    queryset = serializers.Constant.objects.all().order_by('constant_name')
    serializer_class = serializers.ConstantSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = serializers.User.objects.all().order_by('id_user_tg')
    serializer_class = serializers.UserSerializer


class UserQuizeViewSet(viewsets.ModelViewSet):
    queryset = serializers.UserQuize.objects.all().order_by('id')
    serializer_class = serializers.UserQuizeSerializer


class UserAnswerViewSet(viewsets.ModelViewSet):
    queryset = serializers.UserAnswer.objects.all().order_by('id')
    serializer_class = serializers.UserAnswerSerializer


class LevelUserViewSet(viewsets.ModelViewSet):
    queryset = serializers.LevelUser.objects.all().order_by('id')
    serializer_class = serializers.LevelUserSerializer


class AccesUserViewSet(viewsets.ModelViewSet):
    queryset = serializers.AccesUser.objects.all().order_by('id')
    serializer_class = serializers.AccesUserSerializer


class QuizeAnswerViewSet(viewsets.ModelViewSet):
    queryset = serializers.QuizeAnswer.objects.all().order_by('id')
    serializer_class = serializers.QuizeAnswerSerializer


class QuizeQuestionViewSet(viewsets.ModelViewSet):
    queryset = serializers.QuizeQuestion.objects.all().order_by('id')
    serializer_class = serializers.QuizeQuestionSerializer


class QuizeTrueAnswerViewSet(viewsets.ModelViewSet):
    queryset = serializers.QuizeTrueAnswer.objects.all().order_by('id')
    serializer_class = serializers.QuizeTrueAnswerSerializer


class StatusQuizeViewSet(viewsets.ModelViewSet):
    queryset = serializers.StatusQuize.objects.all().order_by('id')
    serializer_class = serializers.StatusQuizeSerializer
