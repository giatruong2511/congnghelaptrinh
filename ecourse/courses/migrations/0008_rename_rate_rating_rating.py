# Generated by Django 3.2.12 on 2022-03-24 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_action_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='rate',
            new_name='rating',
        ),
    ]
