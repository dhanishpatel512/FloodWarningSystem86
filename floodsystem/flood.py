from .utils import sorted_by_key
import matplotlib.pyplot as plt
import numpy as np


def stations_level_over_threshold(stations, tol):
    """Returns a list stations higher than rtol and the relative water level at the station"""
    # Create a list of stations above tolerance
    stations_level_over_thr = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                stations_level_over_thr.append((station, station.relative_water_level()))

    a = sorted_by_key(stations_level_over_thr, 1, reverse=True)
    return a


def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest"""
    # Create list with the stations
    stations_with_relative_level = []
    # Use previous function to get list of tuples of stations with relative water level
    stations_with_relative_level = stations_level_over_threshold(stations, 0)

    a = sorted_by_key(stations_with_relative_level, 1, reverse=True)

    # Return first N values
    return a[:N]


def plot_water_levels(station, dates, levels):
    """Plots the water level at different dates for a given station."""
    # Plot
    plt.plot(dates, levels)
    line_low, = plt.plot(dates, np.full(len(dates), station.typical_range[0]), 'r--', label='Typical low level')
    line_high, = plt.plot(dates, np.full(len(dates), station.typical_range[1]), 'b--', label='Typical high level')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(handles=[line_low, line_high])

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()