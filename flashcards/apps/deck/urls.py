from django.urls import path

from .views import DeckListView, DeckCreateView

app_name = 'deck'

urlpatterns = [
    path('', DeckListView.as_view(), name='index'),
    path('create/', DeckCreateView.as_view(), name='create'),
]
