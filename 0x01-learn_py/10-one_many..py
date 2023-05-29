#!/usr/bin/env python3

from django.db import models


class Artist(models.Model):
    """an Artist"""
    name = models.CharField(max_length=128, db_index=True, help_text='Artist')

    def __str__(self) -> str:
        """str rep'n of Model object"""
        return self.title


class Album(models.Model):
    """an Album"""
    title = models.CharField(max_length=128, db_index=True, help_text='Album Title')
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """str rep'n of Model object"""
        return self.title


class Genre(models.Model):
    """a Genre"""
    name = models.CharField(max_length=128, db_index=True, help_text='Genre')

    def __str__(self) -> str:
        """str rep'n of Model object"""
        return self.title


class Track(models.Model):
    """a Track"""
    title = models.CharField(max_length=128, db_index=True, help_text='Track')
    rating = models.IntegerField(null=True)
    length = models.IntegerField(null=True)
    count = models.IntegerField(null=True)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        """str rep'n of Model object"""
        return self.title
