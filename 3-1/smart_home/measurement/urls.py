from django.urls import path, include
from django.contrib import admin

from rest_framework import routers
from measurement.views import SensorViewSet, MeasurementViewSet


router = routers.DefaultRouter()

router.register('sensor', SensorViewSet)
router.register('measurement', MeasurementViewSet)



urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты

    path('admin/', admin.site.urls),

    path('api/<pk>/', include(router.urls)),

]
