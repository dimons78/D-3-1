from rest_framework.viewsets import ModelViewSet

from .serializers import MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement




class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer