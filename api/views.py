from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserTenant, Task
from .calculate_distances import get_coordinates, calculate_distance

class CalculateDistanceView(APIView):
    def get(self, request):
        # Retrieve the "City" attribute values for a "UserTenant" and a "Task" instance
        user_tenant = UserTenant.objects.first()
        task = Task.objects.first()

        # Use a geocoding service (e.g., Google Maps Geocoding API) to obtain the latitude and longitude coordinates
        user_tenant_coordinates = get_coordinates(user_tenant.city)
        task_coordinates = get_coordinates(task.city)

        # Calculate the distance between the two points
        distance = calculate_distance(user_tenant_coordinates, task_coordinates)

        # Return the calculated distance as a response from the API view
        return Response({'distance': distance})


def distance(request):
    return render(request, 'distance.html')





