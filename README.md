# PyPascal

This is all just for fun / education. It's my first use of `Python`. The project generates an image of Sierpinski's Gasket.

## Running
From the root of the repository, run the following command

    python pascalfun.py 300 > ~/hosthome/test/pythonimage.json

This command generates a 300 x 300 pixel image of Sierpinski's Gasket, and pipes the resulting JSON image data to a file. The resulting file format is the [Simple Image](https://github.com/adamedx/simple-image-demo) format.

### How it works
The approach used to generate Sierpinski's Gasket is to actually generate Pascal's triangle (hence the name of the project) using a modulus of 2 or greater. The application of the modulus happens to result in Sierpinski's Gasket. :) 

Additionally, the modulus ensures that we don't encounter an overflow with the integer arithmetic operations used to generate succesive rows of Pascal's triangle.

### Classes
The project implements the following Python classes that could be reused in other contexts:

* `Pascal`: Generates Pascal's triangle with a given modulus.
* `Rainbow`: This class maps an integer index to points along an imagined continuum of RGB color values that vary as the colors of a rainbow.
* `SimpleImage`: This class enables the creation of of a two-dimensional image representation described by RGB color pixels.
* `ImageWriter`: Serializes a `SimpleImage` image representation.
* `PascalFun`: This is the least reusable class since it also contains user interaction logic. This class uses all the others to get input about the image parameters, generate the image, and then serialize it.

License and Authors
-------------------
Copyright:: Copyright (c) 2016 Adam Edwards

License:: Apache License, Version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
