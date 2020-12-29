# Import numpy as np
import numpy as np
from population import pop
from gdp_cap import gdp_cap
from life_exp import life_exp
import matplotlib.pyplot as plt

# Store pop as a numpy array: np_pop

np_pop = np.array(pop)

# Double np_pop
np_pop=np_pop*2


# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

# # Scatter plot
# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)
#
# # Previous customizations
# plt.xscale('log')
# plt.xlabel('GDP per Capita [in USD]')
# plt.ylabel('Life Expectancy [in years]')
# plt.title('World Development in 2007')
# plt.xticks([1000,10000,100000], ['1k','10k','100k'])
#
# # Additional customizations
# plt.text(1550, 71, 'India')
# plt.text(5700, 80, 'China')
#
# # Add grid() call
# plt.grid(True)
#
# # Show the plot
# plt.show()