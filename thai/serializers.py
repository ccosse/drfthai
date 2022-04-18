from rest_framework import serializers
from django.contrib.auth.models import User
from thai.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    phrases = serializers.HyperlinkedRelatedField(many=True, view_name='phrase-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'phrases']

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Phrase
        fields = ['url','id','owner','title','data']
