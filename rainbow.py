#
# Rainbow
#
# Copyright 2017, Adam Edwards
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math

class Rainbow:

    RED_SOURCE_LOCATION = 0;
    BLUE_SOURCE_LOCATION = 2 * math.pi / 3;
    GREEN_SOURCE_LOCATION = (2 * math.pi / 3) * 2;
    MAX_DISTANCE = 2;

    @classmethod
    def get_color_from_offset(cls, offset, paletteSize):
        colorCount = 1 << 23
        colorIndex = offset % paletteSize

        # Generate palette by modeling light mixing along a unit circle
        # that contains 3 lights at points equidistant from each other
        location = (2 * math.pi / paletteSize) * colorIndex
        redDistance = cls.__get_polar_distance_on_unit_circle(cls.RED_SOURCE_LOCATION, location)
        greenDistance = cls.__get_polar_distance_on_unit_circle(cls.GREEN_SOURCE_LOCATION, location)
        blueDistance = cls.__get_polar_distance_on_unit_circle(cls.BLUE_SOURCE_LOCATION, location)

        return ((int((cls.MAX_DISTANCE - redDistance) * 255) % 256),
                (int((cls.MAX_DISTANCE - greenDistance) * 255) % 256),
                (int((cls.MAX_DISTANCE - blueDistance) * 255) % 256))

    @classmethod
    def __get_polar_distance_on_unit_circle(cls, radians1, radians2):
        # Distance in polar coordinates is
        # D = sqrt(r1^2 + r2^2 - 2 * r1 * r2 * cos(theta1 - theta2))
        #
        # Here, both points are on unit circle, so r1 = r2 = 1
        return math.sqrt(2 - 2 * math.cos(radians1 - radians2))

