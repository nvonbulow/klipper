# Code for handling the kinematics of cartesian robots
#
# Copyright (C) 2018 Nick von Bulow <nick@nvonbulow.com>
#
# This file may be distributed under the terms of the GNU GPLv3 license.

from copy import deepcopy


# Base class where every
class Leveling:
    def __init__(self, kinematics, printer, limits, config):
        self.kin = kinematics
        self.printer = printer
        self.limits = limits
        self.grid_size = (config.getint('grid_points_x', 3),
                          config.getint('grid_points_y', 3))
        # Need to still set config options for a manual measure
        self.grid = [[0.] * self.grid_size[1]] * self.grid_size[0]
        self.padding = (config.getfloat('padding_x', 0),
                        config.getfloat('padding_y', 0))
        self.probe_height = config.getfloat('probe_height', 5)

    def height_offset(self, position):
        return 0

    def set_grid(self, grid):
        if len(grid) != self.grid_size[1] or len(grid[0]) != self.grid_size[0]:
            raise AssertionError('Size of new leveling grid does not equal proper dimensions')
        self.grid = deepcopy(grid)

    def reset_grid(self):
        self.grid = [[0.] * self.grid_size[1]] * self.grid_size[0]


class NoLeveling(Leveling):
    def __init__(self, kinematics, printer, limits, config):
        Leveling.__init__(self, kinematics, printer, limits, config)

    def height_offset(self, position):
        return 0


class BilinearLeveling(Leveling):
    def __init__(self, kinematics, printer, limits, config):
        Leveling.__init__(self, kinematics, printer, limits, config)

    def height_offset(self, position):
        return 0


# Test class that simply adds one to every coordinate
class HighLeveling(Leveling):
    def __init__(self, kinematics, printer, limits, config):
        Leveling.__init__(self, kinematics, printer, limits, config)

    def height_offset(self, position):
        return position[0] * 0.5
