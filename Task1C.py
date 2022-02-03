from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    stations_within_10k_names = []

    # Cambridge City Centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Build list of stations
    stations = build_station_list()

    # Radius
    r = 10

    # Get stations within radius
    stations_within_10k = stations_within_radius(stations, cambridge_city_centre, r)

    for station in stations_within_10k:
        stations_within_10k_names.append(station.name)

    stations_within_10k_names.sort()
    print(stations_within_10k_names)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
