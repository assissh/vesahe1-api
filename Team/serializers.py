from rest_framework import serializers #declearing the serializers to serialize the data of rest
from .models import Development_team,Production_team,Marketing_team#import the model



class Development_teamserializer(serializers.HyperlinkedModelSerializer):#define a class of serializer
    class Meta:

        model = Development_team
        fields = ('Name','Description')#define the fields of model to serialize


class Production_teamserializer(serializers.HyperlinkedModelSerializer):#define a class of serializer
    class Meta:

        model = Production_team
        fields = ('Name','Description')#define the fields of model to serialize


class Marketing_teamserializer(serializers.HyperlinkedModelSerializer):#define a class of serializer
    class Meta:

        model = Marketing_team
        fields = ('Name','Description')#define the fields of model to serialize