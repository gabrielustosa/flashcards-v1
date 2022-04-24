from rest_framework.routers import SimpleRouter

from flashcards.apps.deck.api import view

deck_api_v1_router = SimpleRouter()
deck_api_v1_router.register(
    'deck/api/v1',
    view.DeckAPIViewSet
)

urlpatterns = deck_api_v1_router.urls
