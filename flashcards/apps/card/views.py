from django.views.generic import TemplateView

from flashcards.apps.card.models import Card
from flashcards.apps.deck.models import Deck


class CardView(TemplateView):
    template_name = 'card/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deck_id = self.kwargs.get('deck_id')
        context['deck'] = Deck.objects.get(pk=deck_id)
        return context
