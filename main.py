import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel("x")
plt.xlabel("y")
plt.title('sin&cos')
plt.legend()
plt.show()
