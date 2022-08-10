
import numpy as np
from scipy.stats import norm

N = norm.cdf

# "Correct" implementation taken from 
# https://www.codearmo.com/python-tutorial/options-trading-black-scholes-model

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)

from black_scholes import BlackScholes 

K = 100
r = 0.1
T = 1
sigma = 0.3
S = np.arange(60,140,10)

calls_correct = [BS_CALL(s, K, T, r, sigma) for s in S]
puts_correct = [BS_PUT(s, K, T, r, sigma) for s in S]

calls = [BlackScholes.call(s, K, T, sigma, r) for s in S]
puts = [BlackScholes.put(s, K, T, sigma, r) for s in S]

print(calls_correct)
print(puts_correct)
print(calls)
print(puts)
epsilon = 0.02

def assert_lists_equal(l1, l2, epsilon):
    for x, y in zip(l1, l2):
        assert(abs(x - y) < epsilon)
    print("assert_lists_equal passed")

assert_lists_equal(calls, calls_correct, epsilon)
assert_lists_equal(puts, puts_correct, epsilon)


# AAPL 8/12 165P after close on 8/9/2021
# Underlying trading at 164.92, 3 dte
# Implied vol = 27.25%
# Risk-free rate = 2.80% (10 Year Treasury Rate)
print(BlackScholes.put(164.92, 165, 3/252, .2725, 0.028))

