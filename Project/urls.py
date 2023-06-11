from django.urls import path
from api.views import CalculateDistanceView, distance


urlpatterns = [
    path('api/calculate_distances/', CalculateDistanceView.as_view(), name='calculate_distance'),
    path('distance/', distance, name='distance'),
]







































# from django.urls import path
# from api.views import DistanceAPIView

# urlpatterns = [
#     path('distance/<int:user_id>/<int:task_id>/', DistanceAPIView.as_view(), name='distance'),
# ]



# from django.urls import path
# from api.views import calculate_distance

# urlpatterns = [
#     path('distance/<int:user_id>/<int:task_id>/', calculate_distance, name='distance'),
# ]
