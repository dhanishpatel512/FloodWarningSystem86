from floodsystem.station import MonitoringStation


def build_test_station_list():
    """Returns a list of dummy stations for use in tests."""

    stations = []

    stations.append(MonitoringStation('link1', 'link2', 'Hexham Wydon Water', (54.963311, -2.107819), (-0.029, 0.067),
                                      'Wydon Burn', 'Hexham Wydon Water'))
    stations.append(MonitoringStation('link1', 'link2', 'North Hull Birdsall Av', (53.76052, -0.408546), (0.004, 0.431),
                                      'River Cam', 'North Hull Birdsall Av'))
    stations.append(MonitoringStation('link1', 'link2', 'Lofthouse', (53.726549, -1.518386), (0.247, 1.15),
                                      'Oulton Beck', 'Lofthouse'))
    stations.append(MonitoringStation('link1', 'link2', 'Brampton Moat Side', (54.942516, -2.73365), (0.065, 0.5),
                                      'Oulton Beck', 'Brampton'))
    stations.append(MonitoringStation('link1', 'link2', 'Coniston Church Bridge', (54.368852, -3.075834), (0.7, 1.3),
                                      'Oulton Beck', 'Coniston'))
    stations.append(MonitoringStation('link1', 'link2', 'Caius Park Bridge', (54.352, -3.125834), (1.5, 0.3),
                                      'River Caius', 'Caius'))
    stations.append(MonitoringStation('link1', 'link2', 'Ambleside Rydal Road', (54.433747, -2.965717), None,
                                      'River Caius', 'Ambleside'))

    return stations
