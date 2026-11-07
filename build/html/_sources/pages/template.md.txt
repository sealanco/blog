# Joyful Mathematics Class 1

[https://ncert.nic.in/textbook.php](https://ncert.nic.in/textbook.php)


## Page 21

Exercise 0001 - Python Code:
[https://github.com/sealanco/blog/blob/main/source/codes/print.py](https://github.com/sealanco/blog/blob/main/source/codes/print.py)
```python
print("Hello")
```

Exercise 0002 - LaTeX Code:
```latex
The quadratic formula is given by $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
```

The quadratic formula is given by $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.

```latex
$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) \, e^{2\pi i \xi x} \, d\xi
$$
```

$$
f(x) = \int_{-\infty}^{\infty} \hat{f}(\xi) \, e^{2\pi i \xi x} \, d\xi
$$

Exercise 0003 - Matplotlib Code:
```python
   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 10, 100)
   plt.figure()
   plt.plot(x, np.sin(x), color="tab:blue")
   plt.title("Sine Wave")
   # Save directly as an SVG file
   plt.savefig('my_plot.svg', format='svg', bbox_inches='tight')

```

```{eval-rst}
.. plot::

   import matplotlib.pyplot as plt
   import numpy as np

   x = np.linspace(0, 10, 100)
   plt.figure()
   plt.plot(x, np.sin(x), color="tab:blue")
   plt.title("Sine Wave")
   # Save directly as an SVG file
   plt.savefig('my_plot.svg', format='svg', bbox_inches='tight')

```