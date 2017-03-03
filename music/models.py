from __future__ import unicode_literals

from django.db import models

# Model for the albums contained on the website
class Album(models.Model):
    artist = models.CharField(max_length=150)
    album_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + " - " + self.artist

# Model for the songs contained on the website
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=150)
