def convert_to_months(years):
    return int(years) * 12


if __name__ == '__main__':
    age_in_years = input('Enter age in years: ')
    age_in_months = convert_to_months(age_in_years)
    print(age_in_years, 'years is', age_in_months, 'months')
