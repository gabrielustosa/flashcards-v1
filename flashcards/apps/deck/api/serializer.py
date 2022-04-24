from rest_framework import serializers

from flashcards.apps.deck.models import Deck


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = [
            'name',
            'author',
            'description',
            'cards',
        ]

    cards = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
