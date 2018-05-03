from django.db import models

class Development_team(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class Production_team(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Marketing_team(models.Model):
        Name = models.CharField(max_length=100)
        Description = models.CharField(max_length=100)

        def __str__(self):
            return self.Name