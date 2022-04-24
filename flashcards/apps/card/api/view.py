from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from flashcards.apps.card.api.serializer import CardSerializer
from flashcards.apps.card.models import Card


class CardAPIViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
