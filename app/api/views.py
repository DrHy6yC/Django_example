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
