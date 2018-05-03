"""vesahe1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from login import views
from Team.views import Development_team_view,Production_team_view,Marketing_team_view
from login.views import loginlist

router = routers.DefaultRouter()
router.register('login',views.loginlist)#define a main url of data interaction for rast framework
router.register('development_team',Development_team_view)
router.register('production_team',Production_team_view)
router.register('marketing_team',Marketing_team_view)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/<int:pk>/', views.logindetail.as_view()),

    # define a url for detail view of rest framework which have the parent port of router url

]
