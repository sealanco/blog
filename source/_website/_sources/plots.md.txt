---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Matplotlib Plot Example

Here is a live-rendered Matplotlib plot using `myst-nb`:

```{code-cell} python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Apply Seaborn theme for clean lines and typography
sns.set_theme(style="darkgrid")

# 2. Override colors for a pure black background
plt.rcParams.update(
    {
        "figure.facecolor": "#000000",  # Pure black figure background
        "axes.facecolor": "#000000",  # Pure black plot area background
        "grid.color": "#2a2a2a",  # Subtle gray grid lines visible on black
        "text.color": "#ffffff",  # White text
        "axes.labelcolor": "#ffffff",
        "xtick.color": "#ffffff",
        "ytick.color": "#ffffff",
    }
)

# Create sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y1, label="Sine", linewidth=2.5)
ax.plot(x, y2, label="Cosine", linewidth=2.5, linestyle="--")

ax.set_title("Pure Black Background with Seaborn Styling", fontsize=14, pad=15)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.legend()

plt.show()
```
