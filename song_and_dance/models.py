from django.db import models

# Create your models here.

class Song(models.Model):
    styles = (
        ('foxtrot', 'Foxtrot'),
        ('quickstep', 'Quickstep'),
        ('tango', 'Tango'),
        ('vwaltz', 'Viennese Waltz'),
        ('waltz', 'Waltz'),
        ('chacha', 'Cha Cha'),
        ('east-coast', 'East Coast Swing'),
        ('jive', 'Jive'),
        ('paso-doble', 'Paso Doble'),
        ('rumba', 'Rumba'),
        ('bachata', 'Bachata'),
        ('bolero', 'Bolero'),
        ('mambo', 'Mambo'),
        ('salsa', 'Salsa'),
        ('west-coast', 'West Coast Swing'),
        ('czech-polka', 'Czech Polka'),
        ('merengue', 'Merengue'),
        ('hustle', 'Hustle'),
        ('default', 'Unknown')
    )
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50, null=True, blank=True)
    style = models.CharField(max_length=30, choices=styles, default='default')
    url = models.CharField(max_length=400)
    notes = models.CharField(max_length=160, null=True, blank=True)

    class Meta:
        unique_together = ('style', 'url', 'name')

    def __str__(self):
        return self.name + " [" + self.style + "]"