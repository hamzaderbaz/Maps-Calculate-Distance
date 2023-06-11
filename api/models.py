
from django.db import models

class UserTenant(models.Model):
    city = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

class Task(models.Model):
    city = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)



































# from django.db import models

# class UserTenant(models.Model):
#     city = models.CharField(max_length=100)
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return self.city

# class Task(models.Model):
#     city = models.CharField(max_length=100)
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)

#     def __str__(self):
#         return self.city







# from django.db import models

# class UserTenant(models.Model):
#     city = models.CharField(max_length=100)

# class Task(models.Model):
#     city = models.CharField(max_length=100)
