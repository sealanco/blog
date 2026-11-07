import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.figure()
plt.plot(x, np.sin(x), color="tab:blue")
plt.title("Sine Wave")
# Save directly as an SVG file
plt.savefig('my_plot.svg', format='svg', bbox_inches='tight')