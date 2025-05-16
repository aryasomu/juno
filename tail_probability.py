from scipy.stats import norm

def compute_tail_probability():
    return 1 - norm.cdf(1)
