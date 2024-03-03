from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api import serializers


class QuizeViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.Quize.objects.all().order_by("quize_name")
    serializer_class = serializers.QuizeSerializer


class ConstantViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.Constant.objects.all().order_by("constant_name")
    serializer_class = serializers.ConstantSerializer


class UserViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.User.objects.all().order_by("id_user_tg")
    serializer_class = serializers.UserSerializer


class UserQuizeViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.UserQuize.objects.all().order_by("id")
    serializer_class = serializers.UserQuizeSerializer


class UserAnswerViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.UserAnswer.objects.all().order_by("id")
    serializer_class = serializers.UserAnswerSerializer


class LevelUserViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.LevelUser.objects.all().order_by("id")
    serializer_class = serializers.LevelUserSerializer


class AccesUserViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.AccesUser.objects.all().order_by("id")
    serializer_class = serializers.AccesUserSerializer


class QuizeAnswerViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.QuizeAnswer.objects.all().order_by("id")
    serializer_class = serializers.QuizeAnswerSerializer


class QuizeQuestionViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.QuizeQuestion.objects.all().order_by("id")
    serializer_class = serializers.QuizeQuestionSerializer


class QuizeTrueAnswerViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.QuizeTrueAnswer.objects.all().order_by("id")
    serializer_class = serializers.QuizeTrueAnswerSerializer


class StatusQuizeViewSet(ModelViewSet):
    permission_classes: tuple = (IsAuthenticated,)
    authentication_classes: tuple = (TokenAuthentication,)
    queryset = serializers.StatusQuize.objects.all().order_by("id")
    serializer_class = serializers.StatusQuizeSerializer
