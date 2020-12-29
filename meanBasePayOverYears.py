# Calculate the mean BasePay for a given set of years.

import numpy as np
import pandas as pd

# Get the data
data = pd.read_csv(
    'Refactored_Py_DS_ML_Bootcamp-master/04-Pandas-Exercises/Salaries.csv'
)

def get_years(data, start, end):
    """
        Get the desired years.
        param from int
        param to int

        return DataFrame with desired years
    """
    years = data[(data['Year'] >= start) & (data['Year'] <= end)]

    return years

def get_year_bp_mean(years, year):
    """
        param years DataFrame of desired years
        param year String of year to get mean of

        return yearMean float
    """
    bps = years[years['Year'] == year].BasePay
    yearMean = {'Year': year, 'BasePay': bps.mean()}

    return yearMean


years = get_years(data, 2011, 2015)

for year in np.arange(2011, 2015, 1):
    print(year, '\t', get_year_bp_mean(years, year)['BasePay'])
