from rest_framework import serializers

from flashcards.apps.card.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'front',
            'back',
            'sentence',
            'deck',
        ]
