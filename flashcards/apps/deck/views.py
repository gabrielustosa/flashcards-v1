from django.views.generic import TemplateView


class DeckListView(TemplateView):
    template_name = 'deck/list.html'
