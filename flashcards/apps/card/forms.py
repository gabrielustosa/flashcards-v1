from django import forms
from .models import Card
from ..deck.models import Deck


class CardCreateForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['front', 'back', 'sentence', 'deck']

    def __init__(self, request, *args, **kwargs):
        super().__init__()
        self.fields['deck'].queryset = Deck.objects.filter(author=request.user)
