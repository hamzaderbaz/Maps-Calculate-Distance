# from django.urls import path, include
# from rest_framework import routers
# from api.views import UserTenantViewSet, TaskViewSet, DistanceAPIView

# router = routers.DefaultRouter()
# router.register('user-tenants', UserTenantViewSet)
# router.register('tasks', TaskViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('distance/<int:user_id>/<int:task_id>/', DistanceAPIView.as_view(), name='distance'),
# ]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]