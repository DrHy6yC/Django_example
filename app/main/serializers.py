from rest_framework import serializers

from .models import Quize

class QuizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quize
        fields = ('quize_name', 'quize_description')
