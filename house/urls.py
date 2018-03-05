from django.conf.urls import patterns, url

from .views import HouseList

urlpatterns = patterns(
    '',
    url(r'^$', HouseList.as_view(), name='house-list'),
)
