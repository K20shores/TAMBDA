# Generated by Django 2.1.4 on 2019-01-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_and_dance', '0002_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='notes',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
    ]
