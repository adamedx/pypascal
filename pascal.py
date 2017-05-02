#
# Pascal
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

class Pascal:
    def __init__(self, max_row):
        self.max_row = max_row
        self.triangle = None

    def show(self, target_row = None):
        self.__generate()
        last_row = self.max_row if target_row == None else target_row
        for row in range(0, last_row + 1):
            for item in self.triangle[row]:
                print(str(item) + " ", end='')
            print('')

    def generate(self, modulus):
        self.__generate(modulus)

    def row_count(self):
        return self.max_row + 1

    def row_element_count(self, row):
        return len(self.triangle[row])

    def row_element(self, row, index):
        return self.triangle[row][index]

    def __generate(self, modulus = None):
        if self.triangle == None:
            self.triangle = []
            last_row = None
            for row in range(0, self.max_row + 1):
                self.triangle.append([])
                this_row = self.triangle[row]
                for column in range(0, row + 1):
                    new_element = 1
                    if column > 0 and column < row:
                        new_element = last_row[column - 1] + last_row[column]
                        if modulus != None:
                            new_element %= modulus
                    this_row.append(new_element)
                last_row = self.triangle[row]

