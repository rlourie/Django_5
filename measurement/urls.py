from django.urls import path

from .views import SensorView, DetailSensorView, MeasurementView, UpdateMeasurementView #, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', DetailSensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('measurements/<pk>/', UpdateMeasurementView.as_view()),
]
