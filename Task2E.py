from floodsystem.flood import stations_highest_rel_level, plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    """Run Task 2E deliverable"""
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    stations_at_risk = stations_highest_rel_level(stations, 6)
    for station in stations_at_risk[1:]:
        dt = 10
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
