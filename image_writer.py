#
# Image Writer
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
#

import json
import bson
from PIL import Image

class ImageWriter:

    @classmethod
    def write_to_javascript_string(cls, image):
        return write_json_to_string(image.get_serializable_data, true)

    @classmethod
    def write_binary_file(cls, image, binary_file):
        image_data = bson.dumps(image.get_serializable_image())
        with open(binary_file, 'wb') as output_file:
            output_file.write(image_data)

    @classmethod
    def write_json_to_string(cls, image, javascript = False):
        image_json = json.dumps(image.get_serializable_image())
        javascript_start = "var imageJSON = `" if javascript else ""
        javascript_end = "`" if javascript else ""
        return "{0}{1}{2}".format(javascript_start, image_json, javascript_end)

    @classmethod
    def write_png_file(cls, image, png_file_path):
        image_information = image.get_serializable_image()
        columns = image_information['width']
        rows = image_information['height']
        byte_data_rgba = bytearray()
        for row in range(0, rows):
            for column in range(0, columns):
                pixel_value_argb = image.get_pixel(column, row)
                # Append bytes in the expected RGBA order
                byte_data_rgba.append((pixel_value_argb & 0x00ff0000) >> 16) # red
                byte_data_rgba.append((pixel_value_argb & 0x0000ff00) >> 8)  # green
                byte_data_rgba.append((pixel_value_argb & 0x000000ff) >> 0)  # blue
                byte_data_rgba.append((pixel_value_argb & 0xff000000) >> 24) # alpha

        image_data = Image.frombytes("RGBA", (columns, rows), bytes(byte_data_rgba))
        image_data.save(png_file_path, 'PNG')


