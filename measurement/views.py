# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer


class SensorView(CreateAPIView, ListAPIView):                           # Вывод и создание сенсоров
    serializer_class = SensorSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class DetailSensorView(RetrieveUpdateAPIView, ListAPIView):

    serializer_class = SensorDetailSerializer

    def get_queryset(self):
        queryset = Sensor.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()

# class UpdateSensorView(RetrieveUpdateAPIView):                                   # Изменение сенсора
#     serializer_class = SensorDetailSerializer
#
#     def get_queryset(self):
#         queryset = Sensor.objects.all()
#         return queryset
#
#     def perform_update(self, serializer):
#         serializer.save()


class UpdateMeasurementView(RetrieveUpdateAPIView):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class MeasurementView(CreateAPIView, ListAPIView):
    serializer_class = MeasurementSerializer

    def get_queryset(self):
        queryset = Measurement.objects.all()
        return queryset

    def perform_update(self, serializer):
        serializer.save()


