
from django.urls import path

from .views import FileView, RequestForMonth, RequestForYear, RequestForDay, \
    CoordenadasWithRequest

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload'),
    path('request-day/', RequestForDay.as_view(), name='dia'),
    path('request-mes/', RequestForMonth.as_view(), name='mes'),
    path('request-ano/', RequestForYear.as_view(), name='ano'),
    path('coor/', CoordenadasWithRequest.as_view(), name='coor'),


]