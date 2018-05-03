from rest_framework import viewsets
from rest_framework.views import APIView
from Team.models import Development_team,Production_team,Marketing_team
from .serializers import Development_teamserializer,Production_teamserializer,Marketing_teamserializer
from rest_framework.response import Response


# Create your views here.



class Development_team_view(viewsets.ModelViewSet):#create a class of view for restframework

    queryset = Development_team.objects.all()  # define the model only in "queryset" variable other variable are not allowed in rest
    serializer_class = Development_teamserializer  # define the class of serializers.py only in serializers_class variable other variable are not allowed in rest



class Development_teamdetail(APIView):#APIView argument for display the data

    def get(self, request, pk):#passing the argument of primary keyfor details
        login = Development_team.objects.get(pk=pk)#getting the primary key
        serializers = Development_teamserializer(login, many=False)
        return Response(serializers.data)#return the data from serializers which id collected above




class Production_team_view(viewsets.ModelViewSet):#create a class of view for restframework

    queryset = Production_team.objects.all()  # define the model only in "queryset" variable other variable are not allowed in rest
    serializer_class = Production_teamserializer  # define the class of serializers.py only in serializers_class variable other variable are not allowed in rest



class Production_teamdetail(APIView):#APIView argument for display the data

    def get(self, request, pk):#passing the argument of primary keyfor details
        team = Production_team.objects.get(pk=pk)#getting the primary key
        serializers = Production_teamserializer(team, many=False)
        return Response(serializers.data)#return the data from serializers which id collected above



class Marketing_team_view(viewsets.ModelViewSet):#create a class of view for restframework

    queryset = Marketing_team.objects.all()  # define the model only in "queryset" variable other variable are not allowed in rest
    serializer_class = Marketing_teamserializer  # define the class of serializers.py only in serializers_class variable other variable are not allowed in rest


class Marketing_teamdetail(APIView):#APIView argument for display the data

    def get(self, request, pk):#passing the argument of primary keyfor details
        team = Marketing_team.objects.get(pk=pk)#getting the primary key
        serializers = Marketing_teamserializer(team, many=False)
        return Response(serializers.data)#return the data from serializers which id collected above