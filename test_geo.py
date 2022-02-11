"""Unit test for the geo module"""

from floodsystem.geo import rivers_with_station, stations_by_distance, stations_by_river
from floodsystem.geo import stations_within_radius, rivers_by_station_number, plot_stations
from floodsystem.utils import sorted_by_key
from data_test import build_test_station_list


def test_distance():
    """Test stations_by_distance function works properly"""

    # Cambridge City Centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Build list of test stations
    stations = build_test_station_list()

    # Get distances to the stations
    station_distances = stations_by_distance(stations, cambridge_city_centre)

    # Test output
    assert station_distances[0][0].name == 'North Hull Birdsall Av'
    assert round(station_distances[0][1], 2) == round(176.53842206949852, 2)
    assert station_distances[6][0].name == 'Brampton Moat Side'
    assert round(station_distances[6][1], 2) == round(357.9585386189013, 2)

    # Test that the list is ordered by distance
    assert sorted_by_key(station_distances, 1) == station_distances


def test_rivers_list():
    """Test function rivers_with_station"""

    # Build list of stations
    stations = build_test_station_list()

    # Make list of rivers
    rivers = rivers_with_station(stations)

    # Test output variables
    assert rivers == ['Oulton Beck', 'River Caius', 'River Cam', 'Wydon Burn']
    # Test that the list of rivers is ordered alphabetically
    assert sorted(rivers) == rivers


def test_stations_river():
    """Test function stations_by_river"""

    # Build list of stations
    stations = build_test_station_list()

    # Make dict with rivers and their stations
    rivers_and_stations = stations_by_river(stations)

    # Test output of stations_by_river for River Caius
    assert rivers_and_stations['River Caius'] == ['Caius Park Bridge', 'Ambleside Rydal Road']


def test_stations_within_radius():
    """Test function stations_within_radius"""

    # Build list of stations
    stations = build_test_station_list()

    # Get list of stations within radius
    stations_within_200k = stations_within_radius(stations, (52.2053, 0.1218), 200)

    stations_within_200k_names = []

    for station in stations_within_200k:
        stations_within_200k_names.append(station.name)

    assert stations_within_200k_names == ['North Hull Birdsall Av']


def test_rivers_by_station_number():
    """rivers_by_station_number"""

    # Build list of stations
    stations = build_test_station_list()

    # Get list of first 2 rivers with highest number of stations
    two_rivers_with_most_stations = rivers_by_station_number(stations, 2)[:2]

    assert two_rivers_with_most_stations == [('Oulton Beck', 3), ('River Caius', 2)]


def test_plot():
    """Test for plot function"""

    # Build list of stations
    stations = build_test_station_list()

    # Plot stations
    plot_stations(stations)
