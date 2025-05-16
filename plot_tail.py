import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def plot_tail():
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x)

    plt.plot(x, y, label='Standard Normal PDF')
    plt.fill_between(x, y, where=(x > 1), color='red', alpha=0.5, label='P(Z > 1)')
    plt.axvline(1, color='black', linestyle='--')
    plt.title('Standard Normal Distribution Tail (Z > 1)')
    plt.legend()
    plt.grid(True)
    plt.show()
