from rest_framework import serializers #declearing the serializers to serialize the data of rest
from .models import Login#import the model



class loginerializer(serializers.HyperlinkedModelSerializer):#define a class of serializer
    class Meta:

        model = Login
        fields = ('Username','Password')#define the fields of model to serialize

