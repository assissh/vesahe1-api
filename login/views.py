from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from login.models import Login
from .serializers import loginerializer
from rest_framework.response import Response






class loginlist(viewsets.ModelViewSet):#create a class of view for restframework

    queryset = Login.objects.all()  # define the model only in "queryset" variable other variable are not allowed in rest
    serializer_class = loginerializer  # define the class of serializers.py only in serializers_class variable other variable are not allowed in rest



class logindetail(APIView):#APIView argument for display the data

    def get(self, request, pk):#passing the argument of primary keyfor details
        login = Login.objects.get(pk=pk)#getting the primary key
        serializers = loginerializer(login, many=False)
        return Response(serializers.data)#return the data from serializers which id collected above
