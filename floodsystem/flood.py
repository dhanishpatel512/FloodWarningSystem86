from .utils import sorted_by_key
import matplotlib.pyplot as plt
import numpy as np
from .analysis import polyfit
import matplotlib
from .datafetcher import fetch_measure_levels
import datetime


def stations_level_over_threshold(stations, tol):
    """Returns a list stations higher than rtol and the relative water level at the station"""
    # Create a list of stations above tolerance
    stations_level_over_thr = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                stations_level_over_thr.append((station, station.relative_water_level()))

    return sorted_by_key(stations_level_over_thr, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    """Returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest"""
    # Create list with the stations
    stations_with_relative_level = []
    # Use previous function to get list of tuples of stations with relative water level
    stations_with_relative_level = stations_level_over_threshold(stations, -20)

    top_stations_withlevels = sorted_by_key(stations_with_relative_level, 1, reverse=True)[:N]

    top_stations = []
    for station, relative_level in top_stations_withlevels:
        top_stations.append(station)

    # Return first N values
    return top_stations


def plot_water_levels(station, dates, levels):
    """Plots the water level at different dates for a given station."""
    # Plot
    plt.plot(dates, levels)
    line_high, = plt.plot(dates, np.full(len(dates), station.typical_range[1]), 'b--', label='Typical high level')
    line_low, = plt.plot(dates, np.full(len(dates), station.typical_range[0]), 'r--', label='Typical low level')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(handles=[line_low, line_high])

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level at different dates and a best fit polynomial for a given station."""
    # Plot data
    plt.plot(dates, levels)
    line_high, = plt.plot(dates, np.full(len(dates), station.typical_range[1]), 'b--', label='Typical high level')
    line_low, = plt.plot(dates, np.full(len(dates), station.typical_range[0]), 'r--', label='Typical low level')

    # Construct and plot polynomial
    poly, d0 = polyfit(dates, levels, p)

    poly_line, = plt.plot(dates, poly(matplotlib.dates.date2num(dates) - d0), 'g--', label=f'Polynomial of degree {p}')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.legend(handles=[poly_line, line_high, line_low])

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def flood_risk_assessment(stations):
    """Classifies the stations according to risk of flooding. Returns list of tuples (name, risk level, score)"""
    stations_and_risk = []
    for station in stations:
        # Get polynomial fit
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        if dates != [] and levels != []:
            poly, d0 = polyfit(dates, levels, 4)

            # Check if level is rising or falling (comparing now and now + 12h)
            x = matplotlib.dates.date2num(dates[-1])
            r = poly(x - d0 + 0.5) > 1.1 * poly(x - d0)
            f = poly(x - d0 + 0.5) < 0.9 * poly(x - d0)

            # Use rising/falling as a scaling factor on relative
            if r:
                scaling_factor = 1.2
            elif f:
                scaling_factor = 0.8
            else:
                scaling_factor = 1

            try:
                score = station.relative_water_level() * scaling_factor

                # Classify risk
                if score > 0.85:
                    risk = 'Severe'
                elif score > 0.75:
                    risk = 'High'
                elif score > 0.5:
                    risk = 'Moderate'
                else:
                    risk = 'Low'

                # Append data from this station to the list
                stations_and_risk.append((station.name, score, risk))
            except TypeError:
                pass

    return sorted_by_key(stations_and_risk, 1, reverse=True)
