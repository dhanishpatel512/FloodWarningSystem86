"""Unit test for the geo module"""

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river
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
    assert station_distances[0][1] < station_distances[1][1] < station_distances[2][1] < station_distances[3][1]


def test_rivers_list():
    """Test function rivers_with_station"""

    # Build list of stations
    stations = build_station_list()

    # Make list of rivers
    rivers = rivers_with_station(stations)

    # Test that output variables are of the right type
    assert isinstance(rivers, list)
    assert isinstance(rivers[0], str)

    # Test that the list of rivers is ordered alphabetically
    assert sorted(rivers) == rivers


def test_stations_river():
    """Test function stations_by_river"""

    # Build list of stations
    stations = build_station_list()

    # Make dict with rivers and their stations
    rivers_and_stations = stations_by_river(stations)

    # Test output of stations_by_river for River Cam
    assert rivers_and_stations['River Cam'] == ['Great Chesterford', 'Weston Bampfylde', 'Cambridge Baits Bite', 'Cam',
                                                'Cambridge Jesus Lock', 'Dernford', 'Cambridge']
