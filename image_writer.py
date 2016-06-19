#
# Image Writer
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
#

import json
import bson

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

