from django.conf.urls import url
from django.contrib.auth.views import LoginView, PasswordResetView

from restaurants.views import (
        # restaurant_create_view,
        # restaurant_list_view,
        RestaurantListView,
        RestaurantDetailView,
        RestaurantCreateView,
)

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),

]
