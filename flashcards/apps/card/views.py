from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import TemplateView

from flashcards.apps.card.forms import CardCreateForm
from flashcards.apps.deck.models import Deck


class CardView(TemplateView):
    template_name = 'card/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deck_id = self.kwargs.get('deck_id')
        context['deck'] = Deck.objects.get(pk=deck_id)
        return context


class CardCreateView(TemplateView):
    template_name = 'card/create.html'

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.form = CardCreateForm(request=self.request)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form

        post = request.POST

        card = form.save(commit=False)
        card.front = post.get('front')
        card.back = post.get('back')
        card.sentence = post.get('sentence')
        card.deck = Deck.objects.get(pk=post.get('deck'))
        card.save()

        return redirect('deck:index')

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = self.form
        return context
