# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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
