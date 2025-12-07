import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x) + np.log(x + 3)

# Монотонный участок
a, b = 0, 1.5
x_ref = np.linspace(a, b, 2000)
y_ref = f(x_ref)

for m in range(1, 16):
    x_nodes = np.linspace(a, b, m+1)
    y_nodes = f(x_nodes)
    coeff = np.polyfit(x_nodes, y_nodes, m)
    y_approx = np.polyval(coeff, x_ref)
    err = np.abs(y_ref - y_approx)
    plt.figure(figsize=(6,2))
    plt.plot(x_ref, err)
    plt.title(f'Степень {m}, max ошибка = {np.max(err):.2e}')
    plt.xlabel('x'); plt.ylabel('|ошибка|')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
