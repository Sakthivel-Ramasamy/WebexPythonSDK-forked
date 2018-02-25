# -*- coding: utf-8 -*-
"""Cisco Spark Room data model."""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from .sparkdata import SparkData


__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2016-2018 Cisco and/or its affiliates."
__license__ = "MIT"


class Room(SparkData):
    """Model a Spark 'room' JSON object as a native Python object."""

    def __init__(self, json):
        """Initialize a Room data object from a dictionary or JSON string.

        Args:
            json(dict, basestring): Input dictionary or JSON string.

        Raises:
            TypeError: If the input object is not a dictionary or string.

        """
        super(Room, self).__init__(json)

    @property
    def id(self):
        """The rooms's unique ID."""
        return self._json_data.get('id')

    @property
    def title(self):
        """A user-friendly name for the room."""
        return self._json_data.get('title')

    @property
    def type(self):
        """The type of room (i.e. 'group', 'direct' etc.)."""
        return self._json_data.get('type')

    @property
    def isLocked(self):
        """Whether or not the room is locked and controled by moderator(s)."""
        return self._json_data.get('isLocked')

    @property
    def lastActivity(self):
        """The date and time when the room was last active."""
        return self._json_data.get('lastActivity')

    @property
    def created(self):
        """The date and time when the room was created."""
        return self._json_data.get('created')

    @property
    def creatorId(self):
        """The ID of the person who created the room."""
        return self._json_data.get('creatorId')

    @property
    def teamId(self):
        """The ID for the team with which this room is associated."""
        return self._json_data.get('teamId')
