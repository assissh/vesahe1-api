from django.urls import path
from Team.views import Development_team_view


urlpatterns = [
    path('', Development_team_view),


    # define a url for detail view of rest framework which have the parent port of router url

]
