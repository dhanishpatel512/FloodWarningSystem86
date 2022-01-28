from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Get list of rivers, prints the total number and the first ten
    # (the output of floodsystem.geo.rivers_with_station is already sorted)
    rivers = rivers_with_station(stations)
    total = len(rivers)
    print(total)
    first_rivers = rivers[:10]
    print(f'There are a total of {total} rivers with at least one station. First 10: {first_rivers}')

    # Print stations by selected rivers
    rivers_and_stations = stations_by_river(stations)
    for river in ['River Aire', 'River Cam', 'River Thames']:
        print(river)
        print(rivers_and_stations[river])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
