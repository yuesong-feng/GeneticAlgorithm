import matplotlib.pyplot as plt
import numpy as np
plt.switch_backend("agg")

x = np.linspace(-1, 2, 1000)

y = x * np.sin(10 * np.pi * x) + 2
plt.plot(x, y, label='linear')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

plt.savefig('test.png', format='png')
