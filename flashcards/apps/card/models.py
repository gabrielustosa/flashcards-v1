from django.db import models
from flashcards.apps.deck.models import Deck

from .fields import OrderField


class Card(models.Model):
    front = models.CharField(max_length=50)
    back = models.CharField(max_length=100)
    sentence = models.CharField(max_length=200)
    order = OrderField(for_fields=['deck'])
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
