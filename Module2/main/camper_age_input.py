"""
Program: camper_age_input.py
Author: Jeffery Decker jefferydecker@gmail.com jmdecker1@dmacc.edu
Last date modified: 06/04/2020


The purpose of this program is to accept any input,
convert to a integer type as age_in_years, convert to age_in_months
and output an informational message.
"""

MONTHS_PER_YEAR = 12


def convert_to_months(years):
    return int(years) * MONTHS_PER_YEAR


if __name__ == '__main__':
    age_in_years = input('Enter age in years: ')
    age_in_months = convert_to_months(age_in_years)
    print(age_in_years, 'years is', age_in_months, 'months')
