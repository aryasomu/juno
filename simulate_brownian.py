import numpy as np


def simulate_brownian(n, num_samples):
    t = 1 / n
    threshold = 1 / np.sqrt(n)

    W_t_samples = np.random.normal(loc=0, scale=np.sqrt(t), size=num_samples)
    empirical_prob = np.mean(W_t_samples > threshold)

    return empirical_prob
