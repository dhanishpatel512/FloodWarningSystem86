"""Unit test for the geo module"""

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river
from floodsystem.geo import stations_within_radius, rivers_by_station_number, plot_stations
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key


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
    assert sorted_by_key(station_distances, 1) == station_distances


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


def test_stations_within_radius():
    """Test function stations_within_radius"""

    # Build list of stations
    stations = build_station_list()

    # Get list of stations within radius
    stations_within_10k = stations_within_radius(stations, (52.2053, 0.1218), 10)

    stations_within_10k_names = []

    for station in stations_within_10k:
        stations_within_10k_names.append(station.name)

    assert type(stations_within_10k_names) == list
    assert type(stations_within_10k_names[0]) == str


def test_rivers_by_station_number():

    # Build list of stations
    stations = build_station_list()

    # Get list of first 9 rivers with highest stations
    nine_rivers_with_most_stations = rivers_by_station_number(stations, 9)

    assert type(nine_rivers_with_most_stations) == list
    assert type(nine_rivers_with_most_stations[0]) == tuple
    assert type(nine_rivers_with_most_stations[0][0]) == str
    assert type(nine_rivers_with_most_stations[0][1]) == int


def test_plot():
    """Test for plot function"""

    # Build list of stations
    stations = build_station_list()

    # Plot stations
    plot_stations(stations)
