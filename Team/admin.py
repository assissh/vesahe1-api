from django.contrib import admin

# Register your models here.
from Team.models import Development_team,Production_team,Marketing_team

admin.site.register(Development_team)
admin.site.register(Production_team)
admin.site.register(Marketing_team)