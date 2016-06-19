#
# Pascal fun
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

import sys
import pascal
import rainbow
import simple_image
import image_writer
import click


class PascalFun:

    @classmethod
#    def run(cls, height, sparse, binary_file):
    def run(cls, **kwargs):
        triangle = pascal.Pascal(kwargs['height'] - 1)
        triangle.generate(kwargs['modulus'])
        image = cls.__draw_triangle(triangle, kwargs['sparse'], kwargs['modulus'])
        cls.__write_triangle(image, kwargs['binary_file'])

    @classmethod
    def __draw_triangle(cls, triangle, sparse, modulus):
        height = triangle.row_count()
        image = simple_image.SimpleImage(height, height, sparse, (65535 << 16) + 65535)
        for row in range(0, height):
            for offset in range(0,row + 1):
                color_index = triangle.row_element(row, offset)
                if color_index > 0:
                    rgbColor = rainbow.Rainbow.get_color_from_offset(color_index - 1, modulus)
                    image.set_pixel(offset + height / 2 - row / 2 - ((height + 1) % 2), row, rgbColor[0], rgbColor[1], rgbColor[2])
        return image

    @classmethod
    def __write_triangle(cls, image, binary_file):
        if len(binary_file) == 0:
            json = image_writer.ImageWriter.write_json_to_string(image)
            print(json)
        else:
            image_writer.ImageWriter.write_binary_file(image, binary_file)

@click.command()
@click.argument('height', default=200) #, help='Height of the triangle')
@click.option('--sparse', default=False, is_flag=True) #, help='Enables sparse image output')
@click.option('--binary-file', default='') #, help='Send binary output to the specified file')
@click.option('--modulus', default=2)
def pascal_fun(height, sparse, binary_file, modulus):
    PascalFun.run(height=height, sparse=sparse, binary_file=binary_file, modulus=modulus)

if __name__ == '__main__':
    pascal_fun()

