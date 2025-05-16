from analysis.tail_probability import compute_tail_probability
from analysis.simulate_brownian import simulate_brownian
from analysis.plot_tail import plot_tail
from config import n, num_samples

if __name__ == "__main__":
    print("=== Brownian Supremum ===")

    p = compute_tail_probability()
    print(f"Theoretical P(Z > 1): {p:.5f}")

    empirical = simulate_brownian(n=n, num_samples=num_samples)
    print(f"Empirical P(W_{{1/n}} > 1/sqrt(n)): {empirical:.5f}")

    plot_tail()