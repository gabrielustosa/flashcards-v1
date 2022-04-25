from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from flashcards.apps.deck.models import Deck


class DeckListView(ListView):
    template_name = 'deck/list.html'
    model = Deck
    paginate_by = 6
    context_object_name = 'decks'


class DeckCreateView(CreateView):
    template_name = 'deck/create.html'
    model = Deck
    fields = ['name', 'description']
    success_url = reverse_lazy('deck:index')

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(DeckCreateView, self).form_valid(form)
