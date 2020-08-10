from django.urls import path
from django.views.generic import RedirectView

from .views import RegisterPageView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login')),
    path('signup/', RegisterPageView.as_view(), name='auth-register'),
]