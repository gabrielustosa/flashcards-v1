# Generated by Django 4.0.4 on 2022-04-22 21:00

from django.db import migrations, models
import django.db.models.deletion
import flashcards.apps.card.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front', models.CharField(max_length=50)),
                ('back', models.CharField(max_length=100)),
                ('sentence', models.CharField(max_length=200)),
                ('order', flashcards.apps.card.fields.OrderField()),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.deck')),
            ],
        ),
    ]