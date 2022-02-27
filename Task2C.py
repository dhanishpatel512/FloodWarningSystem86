from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    """Requirements for Task 2C"""

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    N = 10

    # Get list of stations with 10 highest relative water levels
    ten_highest_water_levels = stations_highest_rel_level(stations, N)
    for station in ten_highest_water_levels:
        print(" {}, {}".format(station[0].name, station[1]))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
