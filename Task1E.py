from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def rivers_by_station_number(stations, N):

    # Get a list of all rivers and create empty dict for later
    rivers = rivers_with_station(stations)
    rivers_and_stations = {}

    # Find number of stations by each river and add the river and its number of stations stations to the dict
    for river in rivers:
        stations_by_this_river = []
        for station in stations:
            if station.river == river:
                stations_by_this_river.append(station.name)
        rivers_and_stations[river] = len(stations_by_this_river)
    
    # Change the dictionary to a list of tuples
    a = rivers_and_stations.items()
    list_of_river_and_number = list(a)

    # Order list by number of monitoring stations
    ordered_list_of_river_and_number = sorted_by_key(list_of_river_and_number, 1)

    # Get the last N stations
    n_greatest_number_stations = ordered_list_of_river_and_number[-N:]

    # Return N list of rivers with number of monitoring stations
    return n_greatest_number_stations

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