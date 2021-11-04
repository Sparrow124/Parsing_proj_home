from django.urls import path
from .views import *


urlpatterns = [
    path('', firstview),
    path('parsing/', pars_button, name='parsing')
]
