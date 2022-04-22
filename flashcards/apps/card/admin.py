from django.contrib import admin

from flashcards.apps.card.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'front', 'back', 'order', 'deck']
