"""
Simple program that takes a list of strings that denote 'mines' like Minesweeper
and returns list with strings that includes integer values for number of mines touching each space

Includes unit test
"""

def annotate(minefield):
    # Function body starts here
    mine_numbers = []
    if len(minefield) < 1:
        return minefield
    if len(minefield) == 1 and len(minefield[0]) < 1:
        return minefield
    if len(minefield) > 1:
        if len(minefield[0]) != len(minefield[-1]):
            raise ValueError("The board is invalid with current input.")
        if len(minefield[0]) != len(minefield[1]):
            raise ValueError("The board is invalid with current input.")
    # make empty lists in mine_numbers equal to length of minefield
    for ind in range(len(minefield)):
        mine_numbers.append('')

    # enumerate the list of lists that represents the whole board
    for ind_1, item in enumerate(minefield):
        if len(minefield) > 1:
            # for first row
            above_ = ind_1 - 1
            below_ = ind_1 + 1
            if ind_1 == 0:
                temp_str = ''
                for ind_2, char in enumerate(item):
                    left_ = ind_2 -1
                    right_ = ind_2 +1
                    temp_counter = 0
                    if not char.isspace():
                        if char != '*':
                            raise ValueError("The board is invalid with current input.")
                        temp_str += char
                    if char.isspace():
                        # count spaces below
                        if minefield[below_][ind_2] == '*':
                            temp_counter += 1
                        if ind_2 > 0:
                            if item[left_] == '*':
                                temp_counter += 1
                            if minefield[below_][left_] == '*':
                                temp_counter += 1
                        if ind_2 < len(item)-1:
                            if item[right_] == '*':
                                temp_counter += 1
                            if minefield[below_][right_] == '*':
                                temp_counter += 1
                        if temp_counter > 0:
                            temp_str += str(temp_counter)
                        elif temp_counter == 0:
                            temp_str += char
                mine_numbers[ind_1] += temp_str
            # for last row
            if ind_1 == len(minefield)-1:
                temp_str = ''
                for ind_2, char in enumerate(item):
                    left_ = ind_2 - 1
                    right_ = ind_2 + 1
                    temp_counter = 0
                    if not char.isspace():
                        temp_str += char
                    if char.isspace():
                        # count spaces above
                        if minefield[above_][ind_2] == '*':
                            temp_counter += 1
                        if ind_2 > 0:
                            if item[left_] == '*':
                                temp_counter += 1
                            if minefield[above_][left_] == '*':
                                temp_counter += 1
                        if ind_2 < len(item) - 1:
                            if item[right_] == '*':
                                temp_counter += 1
                            if minefield[above_][right_] == '*':
                                temp_counter += 1
                        if temp_counter > 0:
                            temp_str += str(temp_counter)
                        elif temp_counter == 0:
                            temp_str += char
                mine_numbers[ind_1] += temp_str
            # for middle sections
            if 0 < ind_1 < len(minefield)-1:
                temp_str = ''
                for ind_2, char in enumerate(item):
                    left_ = ind_2 - 1
                    right_ = ind_2 + 1
                    temp_counter = 0
                    if not char.isspace():
                        temp_str += char
                    if char.isspace():
                        # count spaces above and below
                        if minefield[above_][ind_2] == '*':
                            temp_counter += 1
                        if minefield[below_][ind_2] == '*':
                            temp_counter += 1
                        # count spaces to sides and diagonals, if valid
                        if ind_2 > 0:
                            if item[left_] == '*':
                                temp_counter += 1
                            if minefield[above_][left_] == '*':
                                temp_counter += 1
                            if minefield[below_][left_] == '*':
                                temp_counter += 1
                        if ind_2 < len(item)-1:
                            if item[right_] == '*':
                                temp_counter += 1
                            if minefield[above_][right_] == '*':
                                temp_counter += 1
                            if minefield[below_][right_] == '*':
                                temp_counter += 1

                        if temp_counter > 0:
                            temp_str += str(temp_counter)
                        elif temp_counter == 0:
                            temp_str += char
                mine_numbers[ind_1] += temp_str
        if len(minefield) == 1:
            temp_str = ''
            for ind_2, char in enumerate(item):
                left_ = ind_2 - 1
                right_ = ind_2 + 1
                temp_counter = 0
                if not char.isspace():
                    if char != '*':
                        raise ValueError("The board is invalid with current input.")
                    temp_str += char
                if char.isspace():
                    # count spaces below
                    if ind_2 > 0:
                        if item[left_] == '*':
                            temp_counter += 1

                    if ind_2 < len(item) - 1:
                        if item[right_] == '*':
                            temp_counter += 1

                    if temp_counter > 0:
                        temp_str += str(temp_counter)
                    elif temp_counter == 0:
                        temp_str += char
            mine_numbers[ind_1] += temp_str

    return mine_numbers


import unittest

class annotate_test(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(annotate([]),[])

    def test_empty_string(self):
        self.assertEqual(annotate(['  ']), ['  '])

    def test_line(self):
        self.assertEqual(annotate(['  *  ']),[' 1*1 '])

    def test_two_line(self):
        self.assertEqual(annotate(['  *  ','  *  ']), [' 2*2 ',' 2*2 '])

    def test_two_line_2(self):
        self.assertEqual(annotate(['*   *',' *   ']), ['*211*', '2*111'])

    def test_three_line(self):
        self.assertEqual(annotate(["*    "," *   ", "    *"]), ['*21  ', '2*111', '1111*'])

    def test_four_line(self):
        self.assertEqual(annotate(["*     *","***    ","*    * ","****   "]),["*421 1*","***1122","*7532*1","****211"])

    def test_four_line_v2(self):
        self.assertEqual(annotate(["*     *","* *    ","*      ","*  *   "]),["*311 1*","*4*1 11","*4221  ","*21*1  "])

if True:
    unittest.main()

