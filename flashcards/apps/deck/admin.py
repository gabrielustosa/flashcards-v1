from django.contrib import admin

from flashcards.apps.deck.models import Deck


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'author']
