from django.urls import path

from . import views

app_name = 'card'

urlpatterns = [
    path('visualisar/<int:deck_id>/', views.CardView.as_view(), name='view'),
    path('criar/', views.CardCreateView.as_view(), name='create'),
]
