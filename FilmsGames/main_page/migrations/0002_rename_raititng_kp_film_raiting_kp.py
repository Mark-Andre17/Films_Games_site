# Generated by Django 4.0.2 on 2022-02-02 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='raititng_KP',
            new_name='raiting_KP',
        ),
    ]
