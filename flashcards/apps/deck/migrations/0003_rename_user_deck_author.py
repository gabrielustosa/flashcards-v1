# Generated by Django 4.0.4 on 2022-04-22 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0002_deck_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='user',
            new_name='author',
        ),
    ]