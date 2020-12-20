from django.urls import path

from . import views
from .views import VesselListView
urlpatterns = [
    path('', VesselListView.as_view(), name='index'),
]
