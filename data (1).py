import matplotlib.pyplot as plt
import numpy as np  

y_cords = [0] #add points by making a comma and an integer

x_cords = [0] #add points by making a comma and an integer

x_sum = sum(x_cords)

y_sum = sum(y_cords)

slope = y_sum/x_sum
y_intercept = 0

for i in range(1, len(x_cords)):  
  y_intercept = y_intercept + (y_cords[i-1] - (slope * x_cords[i-1]))

y = [(slope * x) + y_intercept for x in x_cords] 

coefficients = np.polyfit(x_cords, y_cords, 1)  
poly = np.poly1d(coefficients)
y_regression = poly(x_cords)  
plt.plot(x_cords, y_cords, label='Original Data')
plt.plot(x_cords, y, label='MAD Line')
plt.plot(x_cords, y_regression, label='Linear Regression')

for x in x_cords:
  label_str = f"Point ({x}, {y_cords[x_cords.index(x)]})"
  plt.scatter(x, y_cords[x_cords.index(x)], color='red', label=label_str)

plt.legend()
plt.show()
