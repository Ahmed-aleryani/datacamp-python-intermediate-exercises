# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]
#
# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]
#
# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc["MOR",["drives_right"]])

# Print sub-DataFrame
print(cars.loc[["RU","MOR"],["country","drives_right"]])