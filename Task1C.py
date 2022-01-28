from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1C"""

    # Cambridge City Centre coordinates
    cambridge_city_centre = (52.2053, 0.1218)

    # Build list of stations
    stations = build_station_list()

    # Radius
    r = 10

    # Get stations within radius
    stations_within_10k = stations_within_radius(stations, cambridge_city_centre, r)

    print(stations_within_10k.sort())

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()