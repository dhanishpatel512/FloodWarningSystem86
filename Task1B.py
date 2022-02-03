from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    # Cambridge City Centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Build list of stations
    stations = build_station_list()

    # Get distances to the stations
    station_distances = stations_by_distance(stations, cambridge_city_centre)

    # Print data of 10 closest stations
    ten_closest_stations = station_distances[:10]
    ten_closest_data = []
    for station, distance in ten_closest_stations:
        ten_closest_data.append((station.name, station.town, distance))
    print('Ten closest stations from Cambridge City Centre:')
    print(ten_closest_data)

    # Print data of 10 furthest stations
    ten_furthest_stations = station_distances[-10:]
    ten_furthest_data = []
    for station, distance in ten_furthest_stations:
        ten_furthest_data.append((station.name, station.town, distance))
    print('Ten furthest stations from Cambridge City Centre:')
    print(ten_furthest_data)


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
