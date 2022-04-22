from django.views.generic import TemplateView

from flashcards.apps.deck.models import Deck


class DeckListView(TemplateView):
    template_name = 'deck/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['decks'] = Deck.objects.all()
        return context
