# -*- coding: utf-8 -*-
"""Incremental VaR

"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

np.random.seed(0)
n_obs = 1000
mu_assets = np.array([0.0005, 0.0003])
sigma_assets = np.array([0.01, 0.015])
corr = 0.6
cov_matrix = np.array([
    [sigma_assets[0]**2, corr*sigma_assets[0]*sigma_assets[1]],
    [corr*sigma_assets[0]*sigma_assets[1], sigma_assets[1]**2]
])

returns = np.random.multivariate_normal(mu_assets, cov_matrix, size=n_obs)

weights_base = np.array([0.6, 0.4])
weights_new = np.array([0.5, 0.5])  # Change portfolio weights

confidence_level = 0.95
z = stats.norm.ppf(confidence_level)

portfolio_returns_base = returns @ weights_base
mu_base = np.mean(portfolio_returns_base)
sigma_base = np.std(portfolio_returns_base)
var_base = -(mu_base + z * sigma_base)

portfolio_returns_new = returns @ weights_new
mu_new = np.mean(portfolio_returns_new)
sigma_new = np.std(portfolio_returns_new)
var_new = -(mu_new + z * sigma_new)

incremental_var = var_new - var_base

data = pd.DataFrame({
    'Portfolio': ['Base', 'Modified'],
    'VaR': [var_base, var_new]
})

plt.figure(figsize=(8,5))
sns.barplot(x='Portfolio', y='VaR', data=data, palette='coolwarm')
plt.title("Incremental VaR Comparison")
plt.ylabel("VaR (95%)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

