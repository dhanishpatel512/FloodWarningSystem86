from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import flood_risk_assessment


def run():
    """Requirements for Task 2G"""

    # Build list of stations
    stations = build_station_list()

    # For demonstration purposes, to save time, 50 stations are analysed
    fifty_stations = stations[:50]

    # Update latest level data for all stations
    update_water_levels(fifty_stations)

    results = flood_risk_assessment(fifty_stations)
    for result in results:
        print(f'Station: {result[0]}, score: {result[1]}, risk: {result[2]}')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
