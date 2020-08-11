from django.urls import path
from django.views.generic import RedirectView
from .views import CalibrationCreateView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core-index')),
    path('calibration/add/', CalibrationCreateView.as_view(), name='inspection-calibration')
]