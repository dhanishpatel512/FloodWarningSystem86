from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from data_test import build_test_station_list


def test_stations_level_over_threshold():

    # Build list of stations
    stations = build_test_station_list()

    tol = 0.6

    # Get list of stations with relative water level above tolerance
    stations_above_tol = stations_level_over_threshold(stations, tol)

    assert stations_above_tol[0][0].name == "Hexham Wydon Water"
    assert round(stations_above_tol[0][1], 2) == round(5.510416666666667, 2)
    assert stations_above_tol[-1][0].name == "North Hull Birdsall Av"
    assert round(stations_above_tol[-1][1], 2) == round(0.6932084309133489, 2)


def test_stations_highest_rel_level():

    # Build list of stations
    stations = build_test_station_list()

    # Get list of stations with top 3 highest relative water levels
    top_three_test = stations_highest_rel_level(stations, 3)

    assert top_three_test[0].name == 'Hexham Wydon Water'
    assert top_three_test[1].name == 'Coniston Church Bridge'
    assert top_three_test[2].name == 'Brampton Moat Side'
