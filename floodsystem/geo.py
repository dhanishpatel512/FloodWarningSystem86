# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from turtle import distance
from .utils import sorted_by_key  # noqa
from haversine import haversine
import plotly.graph_objects as go


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


def plot_stations(stations):
    """Plots the stations on a map using Plotly and Mapbox"""

    # Get lists of strings with lats, longs and station names
    lats, longs, texts = [], [], []
    for station in stations:
        lats.append(str(station.coord[0]))
        longs.append(str(station.coord[1]))
        texts.append(station.name)

    # Get Mapbox token
    mapbox_access_token = open(".mapbox_token").read()

    # Create figure with data above
    fig = go.Figure(go.Scattermapbox(lat=lats, lon=longs, mode='markers', marker=go.scattermapbox.Marker(size=9),
                    text=texts))

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=52.62,
                lon=-1.14
            ),
            pitch=0,
            zoom=5
        ),
    )

    fig.show()
