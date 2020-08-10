from django.urls import path
from .views import HomePageView, NDEFormsView

urlpatterns = [
    path('', HomePageView.as_view(), name='core-index'),
    path('nde', NDEFormsView.as_view(), name='core-nde-forms'),
]