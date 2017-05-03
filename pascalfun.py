#
# Pascal fun
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

import sys
import pascal
import rainbow
import simple_image
import image_writer
import click


class PascalFun:

    @classmethod
    def run(cls, **kwargs):
        cls.__validate_arguments(kwargs)
        triangle = pascal.Pascal(kwargs['height'] - 1)
        triangle.generate(kwargs['modulus'])
        image = cls.__draw_triangle(triangle, kwargs['sparse'], kwargs['modulus'], kwargs['background_argb_hex_color'])
        cls.__write_triangle(image, kwargs['output_path'], kwargs['output_type'])

    @classmethod
    def __validate_arguments(cls, arguments):
        output_type = arguments['output_type']
        if output_type == 'bson' or output_type == 'png':
            if len(arguments['output_path']) == 0:
                raise ValueError('a binary output type of \'{output_type}\' was specified without specifying --output-path.'.format(output_path))
        background_color = int(arguments['background_argb_hex_color'], 16)
        if background_color < 0 or background_color > int('0xFFFFFFFF', 16):
            raise ValueError("Value '{0}' for --background-argb-hex-color option is not a valid 32-bit unsigned integer".format(background_color))

    @classmethod
    def __draw_triangle(cls, triangle, sparse, modulus, background_color_hex_string):
        height = triangle.row_count()
        image = simple_image.SimpleImage(height, height, sparse, int(background_color_hex_string, 16))
        for row in range(0, height):
            for offset in range(0, row + 1):
                color_index = triangle.row_element(row, offset)
                if color_index > 0:
                    rgbColor = rainbow.Rainbow.get_color_from_offset(color_index - 1, modulus)
                    image.set_pixel(int(offset + height / 2 - row / 2 - ((height + 1)) % 2), row, rgbColor[0], rgbColor[1], rgbColor[2])
        return image

    @classmethod
    def __write_triangle(cls, image, binary_file, output_type):
        if len(binary_file) == 0:
            json = image_writer.ImageWriter.write_json_to_string(image, output_type == 'javascript_output')
            print(json)
        elif output_type == 'bson':
            image_writer.ImageWriter.write_binary_file(image, binary_file)
        elif output_type == 'png':
            image_writer.ImageWriter.write_png_file(image, binary_file)
        else:
            raise ValueError('an invalid binary output type of \'{output_type}\' was specified.'.format(output_path))

@click.command()
@click.argument('height', default=int(200)) #, help='Height of the triangle (default 200)')
@click.option('--sparse', default=False, is_flag=True, help='Enables sparse image output')
@click.option('--modulus', default=2, help='Modulus with which to scale elements of Pascal\'s triangle (default 2)')
@click.option('--background-argb-hex-color', default='0x00000000', help='Background color in ARGB hexadecimal format to which all pixels are initialized')
@click.option('--output-path', default='', help='Send output to the specified path')
@click.option('--output-type', type=click.Choice(['json', 'bson', 'png', 'javascript']), default='json', help='Send output in the specified format (default is json to standard output)')
def pascal_fun(height, sparse, modulus, background_argb_hex_color, output_path, output_type):
    """This script generates Pascal's triangle as variants of Simple Image Format or other graphic formats."""
    PascalFun.run(height=height, modulus=modulus, background_argb_hex_color=background_argb_hex_color, sparse=sparse, output_path=output_path, output_type=output_type)

if __name__ == '__main__':
    pascal_fun()

