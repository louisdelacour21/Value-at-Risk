# -*- coding: utf-8 -*-
"""Parametric Normal VaR
Variance-Covariance VaR (Parametric Normal VaR)
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

returns = np.array([-2.1, -0.9, 0.2, -1.3, 1.5, -0.3, -2.7, 0.7, -1.9, 0.4]) / 100
confidence_level = 0.95
percentile = 100 * (1 - confidence_level)

# Mean and std of returns
mu = np.mean(returns)
sigma = np.std(returns)
z = stats.norm.ppf(confidence_level)
parametric_var = -(mu + z * sigma)

# Normal distribution plot
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
pdf = stats.norm.pdf(x, mu, sigma)

plt.figure(figsize=(10, 6))
plt.plot(x, pdf, label='Normal Distribution')
plt.axvline(-parametric_var, color='purple', linestyle='--', label=f'VaR ({confidence_level*100:.0f}%) = {-parametric_var:.2%}')
plt.fill_between(x, pdf, where=(x <= -parametric_var), color='purple', alpha=0.3)
plt.title('Parametric VaR (Variance-Covariance)')
plt.xlabel('Returns')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
