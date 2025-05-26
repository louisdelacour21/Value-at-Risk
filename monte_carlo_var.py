# -*- coding: utf-8 -*-
"""Monte carlo VaR
"""

import numpy as np
import matplotlib.pyplot as plt
#parameters
initial_value = 1_000_000
mu_mc = 0.0005
sigma_mc = 0.02
n_simulations = 100_000
confidence_level = 0.95

# Simulations
simulated_returns = np.random.normal(mu_mc, sigma_mc, n_simulations)
portfolio_end_values = initial_value * (1 + simulated_returns)
losses = initial_value - portfolio_end_values

# VaR
monte_carlo_var = np.percentile(losses, 100 * (1 - confidence_level))

# Plot
plt.figure(figsize=(10, 6))
plt.hist(losses, bins=100, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(monte_carlo_var, color='darkgreen', linestyle='--', label=f'VaR = ${monte_carlo_var:,.0f}')
plt.title('Monte Carlo Simulation - Portfolio Losses')
plt.xlabel('Losses')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

