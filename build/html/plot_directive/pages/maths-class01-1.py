import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure()
plt.plot(x, np.sin(x), color="tab:blue")
plt.title("Sine Wave")