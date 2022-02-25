from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """Returns a list stations higher than rtol and the relative water level at the station"""
    # Create a list of stations above tolerance
    stations_level_over_thr = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                stations_level_over_thr.append((station, station.relative_water_level()))

    a = sorted_by_key(stations_level_over_thr, 1)
    a.reverse()
    return a
