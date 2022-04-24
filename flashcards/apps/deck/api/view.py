from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from flashcards.apps.deck.api.serializer import DeckSerializer
from flashcards.apps.deck.models import Deck


class DeckAPIViewSet(ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    pagination_class = PageNumberPagination
    http_method_names = ['get', 'options', 'head']
