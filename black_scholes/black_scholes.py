
import numpy as np
from scipy.stats import norm


class BlackScholes:
    """
    Does not account for dividends or early exercise. 
    """
    @staticmethod
    def call(S, K, t, sigma, r):
        d1 = (np.log(S/K) + (r + (sigma**2/2)) * t)/(sigma * np.sqrt(t))
        d2 = d1 - sigma * np.sqrt(t)
        return norm.cdf(d1) * S - norm.cdf(d2) * K * np.exp(-r * t)

    @staticmethod 
    def put(S, K, t, sigma, r):
        d1 = (np.log(S/K) + (r + (sigma**2/2)) * t)/(sigma * np.sqrt(t))
        d2 = d1 - sigma * np.sqrt(t)
        return -norm.cdf(-d1) * S + norm.cdf(-d2) * K * np.exp(-r * t)



