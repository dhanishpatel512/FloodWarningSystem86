"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance, plot_stations
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list


def test_distance():
    """Test stations_by_distance function works properly"""

    # Cambridge City Centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Build list of stations
    stations = build_station_list()

    # Get distances to the stations
    station_distances = stations_by_distance(stations, cambridge_city_centre)

    # Test that output variables are of the right type
    assert isinstance(station_distances[0][0], MonitoringStation)
    assert isinstance(station_distances[0][1], float)

    # Test that the list is ordered by distance
    assert station_distances[0][1] < station_distances[1][1]


def test_plot():
    # Build list of stations
    stations = build_station_list()

    # Plot stations
    plot_stations(stations)
