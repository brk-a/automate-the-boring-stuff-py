#!/usr/bin/env python3

'''
Why write SQL when you can write Py? It is easy!
Rebuttal: Why write Py when you can write SQL? It
is system and db-agnostic, to begin with!
'''

from django.db import models


class Users(models.Model):
    """
    Users table

    SQL equivalent of:
    CREATE TABLE Users(
        name: VARCHAR(128),
        email: VARCHAR(128)
    );
    """
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)

