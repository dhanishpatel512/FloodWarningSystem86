from floodsystem.stationdata import build_station_list
from floodsystem.geo import plot_stations


def run():
    """Extension to plot all stations on a map"""

    # Build list of stations
    stations = build_station_list()

    # Plot stations
    plot_stations(stations)


if __name__ == "__main__":
    print("*** Extension task: CUED Part IA Flood Warning System ***")
    run()
