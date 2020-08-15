from django.urls import path
from django.views.generic import RedirectView
from .views import InspectionCreateView, AJAXInspectionEndPoint

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core-index')),
    # path('calibration/add/', InspectionCreateView.as_view(), name='inspection-calibration'),
    path('add/', InspectionCreateView.as_view(), name='inspection-add-inspection'),
    path('api/', AJAXInspectionEndPoint.as_view(), name='inspection-ajax-api')
]