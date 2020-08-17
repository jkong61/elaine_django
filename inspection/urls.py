from django.urls import path
from django.views.generic import RedirectView
from .views import InspectionCreateView,InspectionDetailView, AJAXInspectionEndPoint

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='core-index')),
    path('add/', InspectionCreateView.as_view(), name='inspection-add-inspection'),
    path('api/', AJAXInspectionEndPoint.as_view(), name='inspection-ajax-api'),
    path('certs/<uuid:pk>', InspectionDetailView.as_view(), name='inspection-detail')
]