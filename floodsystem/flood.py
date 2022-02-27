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


def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest"""
    # Create list with the stations
    stations_with_relative_level = []
    # Use previous function to get list of tuples of stations with relative water level
    stations_with_relative_level = stations_level_over_threshold(stations, 0)

    a = sorted_by_key(stations_with_relative_level, 1)
    a.reverse()

    # Return first N values
    return a[:N]
