# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """Returns a list containing all the stations and their distance from a point p."""

    station_distances = []
    for station in stations:
        # Calculate the distance using the Haversine formula
        distance = haversine(station.coord, p)
        station_distances.append((station, distance))

    # Return the list sorted by distance
    return sorted_by_key(station_distances, 1)


def rivers_with_station(stations):
    """Returns a list containing the names of all the rivers that have at least one of the stations provided as input"""

    # Add the rivers of all stations to a set so they are not repeated.
    rivers = set()
    for station in stations:
        rivers.add(station.river)

    # Return rivers ordered alphabetically
    return sorted(list(rivers))


def stations_by_river(stations):
    """Returns a dictionary that maps the river names to the list of stations by the river."""

    # Get a list of all rivers and create empty dict for later
    rivers = rivers_with_station(stations)
    rivers_and_stations = {}

    # Find stations by each river and add the river and its stations to the dict
    for river in rivers:
        stations_by_this_river = []
        for station in stations:
            if station.river == river:
                stations_by_this_river.append(station.name)
        rivers_and_stations[river] = stations_by_this_river

    # Return dict with output
    return rivers_and_stations
