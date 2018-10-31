from django.urls import path

from gif.views.roulette import Roulette

app_name = 'gif'

urlpatterns = [
    path('roulette/', Roulette.as_view(), name='roulette'),
]
