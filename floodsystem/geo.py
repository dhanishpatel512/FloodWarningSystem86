# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from turtle import distance
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

def stations_within_radius(stations, centre, r):
    """Returns a list of all stations (type MonitoringStation) within radius r of a geographic coordinate x."""

    stations_inside_radius = []
    for station, distance in stations_by_distance(stations, centre):
        # Check if distance is inside the requried radius
        if  distance < r:
            stations_inside_radius.append(station)

    # Return the list 
    return stations_inside_radius