from rest_framework.routers import SimpleRouter

from flashcards.apps.card.api import view

card_api_v1_router = SimpleRouter()
card_api_v1_router.register(
    'card/api/v1',
    view.CardAPIViewSet
)

urlpatterns = card_api_v1_router.urls
