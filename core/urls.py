from django.urls import path
from .views import HomePageView, InstanceCreationView, SuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='core-index'),
    path('addinstance/', InstanceCreationView.as_view(), name='core-add-instance'),
    path('success/', SuccessView.as_view(), name='core-success')
]