import numpy as np
import matplotlib.pyplot as plt

# Vector origin Location
x1 = [0]
y1 = [0]
# Directional vectors
x2 = [3]
y2 = [2]

x3 = [5]
y3 = [-4]
# Creating plot
plt. quiver(x1, y1, x2, y2, color='k', units='xy', scale=1)
plt. quiver(x2, y2, x3, y3, color='b', units='xy', scale=1)
plt. quiver(x1, y1, x2.pop() + x3.pop(), y2.pop() + y3.pop(), color='r', units='xy', scale=1)

#x-Lim and y-Lim
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid()
# Show plot with grid
plt.show()
