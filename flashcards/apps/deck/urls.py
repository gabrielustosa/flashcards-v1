from django.urls import path

from . import views

app_name = 'deck'

urlpatterns = [
    path('', views.DeckListView.as_view(), name='index'),
]
