from life_exp import life_exp
import matplotlib.pyplot as plt
# print(life_exp)

#histegram function
# plt.hist(life_exp)
# plt.show()

# Build histogram with 5 bins
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()

