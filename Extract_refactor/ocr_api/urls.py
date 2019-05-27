
from django.urls import path

from .views import FileView, RequestForMonth, RequestForYear, RequestForDay, \
    CoordenadasWithRequest

from . import views


ocr = views.FileView.as_view({
    'post': 'upload'
})
scrapy = views.WebScrapyView.as_view({
    'post': 'upload'
})

urlpatterns = [
    path('upload/', ocr, name='file-upload'),
    path('scrapy/', scrapy, name='scrapy'),
    path('request-day/', RequestForDay.as_view(), name='dia'),
    path('request-mes/', RequestForMonth.as_view(), name='mes'),
    path('request-ano/', RequestForYear.as_view(), name='ano'),
    path('coor/', CoordenadasWithRequest.as_view(), name='coor'),


]