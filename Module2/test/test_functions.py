"""
Program: test_functions.py
Author: Jeffery Decker jefferydecker@gmail.com jmdecker1@dmacc.edu
Last date modified: 06/04/2020


The purpose of this program is to test the convert_to_months
function from camper_age_input.py
"""


import unittest
from main import camper_age_input
from main.camper_age_input import convert_to_months


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(36, convert_to_months(3))


if __name__ == '__main__':
    unittest.main()
