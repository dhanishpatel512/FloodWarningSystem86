from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Get list of 9 rivers with highest number of monitoring stations
    nine_rivers_with_most_stations = rivers_by_station_number(stations, 9)

    print(nine_rivers_with_most_stations)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
