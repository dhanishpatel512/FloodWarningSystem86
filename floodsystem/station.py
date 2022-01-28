# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town

        self.latest_level = None

    @property
    def station_id(self):
        """Get the station id."""
        return self._station_id

    @property
    def measure_id(self):
        """Get the measure id."""
        return self._measure_id

    @property
    def name(self):
        """Get the name."""
        return self._name

    @property
    def coord(self):
        """Get the coord."""
        return self._coord

    @property
    def typical_range(self):
        """Get the typical range."""
        return self._typical_range

    @property
    def river(self):
        """Get the river."""
        return self._river

    @property
    def town(self):
        """Get the town."""
        return self._town

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
