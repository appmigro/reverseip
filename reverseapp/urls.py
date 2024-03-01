from django.urls import path
from .views import ReverseIPView

urlpatterns = [
    path('', ReverseIPView.as_view(), name='reverse_ip'),
]
