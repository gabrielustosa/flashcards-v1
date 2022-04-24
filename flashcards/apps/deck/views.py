from django.views.generic import ListView

from flashcards.apps.deck.models import Deck


class DeckListView(ListView):
    template_name = 'deck/list.html'
    model = Deck
    paginate_by = 6
    context_object_name = 'decks'

