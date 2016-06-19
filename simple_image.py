#
# Simple Image
#
# Copyright 2016, Adam Edwards
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

class SimpleImage:
    def __init__(self, width, height, is_sparse = False, default_color = 0):
        self.__width = width
        self.__height = height
        self.__sparse_size = 0
        self.__default_color = default_color
        self.__is_sparse = is_sparse
        self.__sparse_map = {}
        self.__image_data = [] if is_sparse else ([default_color] * (width * height))

    def get_pixel(self, x, y):
        pixel_index = self.__get_pixel_index(x, y)
        result = None
        if self.__is_sparse:
            existing_pixel = self.__find_sparse_pixel(pixel_index)
            result = self.__default_color if existing_pixel == None else self.__image_data[existing_pixel + 1]
        else:
            result = self.__image_data[pixel_index]
        return result

    def set_pixel(self, x, y, red, green, blue, alpha = 255):
        pixel_index = self.__get_pixel_index(x, y)
        existing_sparse_offset = (None if self.__is_sparse else self.__find_sparse_pixel(pixel_index))
        image_offset = pixel_index
        if self.__is_sparse:
            if existing_sparse_offset == None:
                image_offset = self.__new_sparse_pixel_offset()
            else:
                image_offset = existing_sparse_offset

        color_offset = 1 if self.__is_sparse else 0
        color = red + (green << 8) + (blue << 16) + (alpha << 24)

        if self.__is_sparse and existing_sparse_offset == None:
            self.__add_sparse_pixel(pixel_index)

        self.__image_data[image_offset + color_offset] = color
        self.__validate_color(x, y, color)

    def get_serializable_image(self):
        return {
            'width':self.__width,
            'height':self.__height,
            'format':(1 if self.__is_sparse else 0),
            'sparseSize':self.__sparse_size,
            'defaultColor':self.__default_color,
            'imageData':self.__image_data
        }

    def __get_pixel_index(self, x, y):
        if x < 0 or x >= self.__width:
            raise ValueError("set_pixel: x coordinate value `{0}` not in the range 0 to {1}".format(x, self.__width - 1))
        if y < 0 or y >= self.__height:
            raise ValueError("set_pixel: y coordinate value `{0}` not in the range 0 to {1}".format(y, self.__height - 1))
        return y * self.__width + x

    def __new_sparse_pixel_offset(self):
        return self.__sparse_size * 2

    def __add_sparse_pixel(self, pixel_index):
        new_offset = self.__new_sparse_pixel_offset()
        self.__image_data.append(pixel_index)
        self.__image_data.append(self.__default_color)
        self.__sparse_map[pixel_index] = new_offset
        self.__sparse_size += 1

    def __find_sparse_pixel(self, pixel_index):
        result = self.__sparse_map[pixel_index] if self.__sparse_map.has_key(pixel_index) else None
        return result

    def __validate_color(self, x, y, color):
        newcolor = self.get_pixel(x, y)
        if newcolor != color:
            raise ValueError("At #{0},#{1} the color should be #{2}, but #{3} was returned".format(x, y, color, newcolor))

