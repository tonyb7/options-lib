Black Scholes 
====
This document is meant to provide a high-level, intuitive overview of Black-Scholes. For a more detailed derivation of the Black-Scholes equation, see [derivation.ipynb](derivation.ipynb).

## The Equation
We begin with the Black-Scholes equation, which is a differential equation describing how the value of an option changes as the underlying price and time changes. The solution to the Black-Scholes equation yields the Black-Scholes model, which is used to calculate the exact value of an option. 

The Black-Scholes equation is given by:

$rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2 C}{\partial S^2}+\frac{\partial C}{\partial t} = rC$

where $C$ is the value of a call, $S$ is the stock price, $t$ is time, $\sigma$ is volatility, and $r$ is the interest rate. 

The above equation describes how changes in $S$ and $t$ affect $C$. Note that $\sigma$ and $r$ are not considered variables, but rather inputs which are assumed to remain constant over the life of the option.

Note that $\frac{\partial C}{\partial S}$ is the option's delta $\Delta$, $\frac{\partial^2 C}{\partial S^2}$ is the option's gamma $\Gamma$, and $\frac{\partial C}{\partial t}$ is the option's theta $\Theta$.


### Interest Rate Components
Black-Scholes values options from the forward price, so the interest rate $r$ gives us:

- Spot-to-forward relationship via the $rS$ term
- Expected-value-to-present-value relationship via the $rC$ term

### Volatility Component
The rate at which delta changes depends on $\Gamma$ and $\sigma$ (the speed at which the stock price is changing). The volatility component and its effect on gamma is given via the $\frac{1}{2}\sigma^2S^2\Gamma$ term.

### Intuition
Suppose we want to estimate the change in an option's value as the underlying price changes from $S_1$ to $S_2$. Using a discrete method, we can estimate the average delta over the price range by

$\Delta_{avg} = \Delta + \frac{1}{2}(S_2-S_1)\Gamma$

Using $\Delta_{avg}$ the price change of the option as the underlying moves from $S_1$ to $S_2$ should be approximately

$(S_2-S_1)\Delta_{avg} = (S_2-S_1)\Delta + \frac{1}{2}(S_2-S_1)^2\Gamma$

Reminding ourselves that $\Delta=\frac{\partial C}{\partial S}$ and $\Gamma=\frac{\partial^2 C}{\partial S^2}$, this looks awfully similar to the first two terms of the Black-Scholes equation, which we can rewrite as $rS\Delta+\frac{1}{2}\sigma^2S^2\Gamma$. 

The primary differences between the equations are the interest-rate component attached to $S$ and the volatility component attached to gamma. The Black-Scholes equation also assumes an instantaneous price change instead of a discrete price change. 

### Derivation
A more detailed derivation can be found in [derivation.ipynb](derivation.ipynb).

## The Formula
The Black-Scholes equation has many solutions, corresponding to all the different derivatives that can be defined with $S$ as the underlying variable. The particular derivative that is obtained when the equation is solved depends on the boundary conditions used. The boundary conditions specify the value of the derivative at the boundaries of possible values of $S$ and $t$. 

For a European call option $C(S_t, t)$ (where the parameters are $S_t$ the price of the underlying and $t$ is time-to-expiry), the boundary conditions are:

1. $C(0, t) = 0 \text{ for all } t$
2. $C(S, t) \rightarrow S - K \text{ as } S\rightarrow\infty$
3. $C(S, 0) = \max\{S - K, 0\}$. This is the value of the option at expiry.

Using these boundary conditions, the Black-Scholes equation can be solved to yield the Black-Scholes formula for the value of a call option:

$$
\begin{aligned}
C(S_t, t) &= \mathcal{N}(d_1)S_t - \mathcal{N}(d_2)Ke^{-rt}\\
d_1 &= \frac{\ln{\frac{S_t}{K}} + (r + \frac{\sigma^2}{2})t}{\sigma\sqrt{t}}\\
d_2 &= d_1 - \sigma\sqrt{t}
\end{aligned}
$$

where 

- $C$ is the theoretical value of a European call
- $t$ is time-to-expiry in years
- $S_t$ is the price of a non-dividend-paying stock with $t$ years until expiry
- $K$ is the strike of the option
- $\sigma$ is the annualized standard deviation (volatility) of the stock price in percent, expressed as a decimal
- $r$ is the annual interest rate, and 
- $\mathcal{N}$ is the cumulative standard normal distribution function.

For a put, we can solve for the formula using different boundary conditions (e.g. $P(S, 0) = \max\{K - S, 0\}$ for the value of the option at expiry), or we can use put-call parity with a discount factor of $e^{-rt}$ to get that 

$$
\begin{aligned}
P(S_t, t) &= Ke^{-rt} - S_t + C(S_t, t) \\
    &= Ke^{-rt} - S_t + (\mathcal{N}(d_1)S_t - \mathcal{N}(d_2)Ke^{-rt})\\
    &= (\mathcal{N}(d_1) - 1)S_t + (1 - \mathcal{N}(d_2))Ke^{-rt}\\
    &= -\mathcal{N}(-d_1)S_t + \mathcal{N}(-d_2)Ke^{-rt}
\end{aligned}
$$

## Sources
- *Option Volatility and Pricing, Chapter 18: The Black-Scholes Model* by Sheldon Natenberg
- [Wikipedia: Black-Scholes Equation](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_equation)
- [FN452 Deriving the Black-Scholes-Merton Equation](https://www.youtube.com/watch?v=IynFtIQ6HaI), Nattakit Chokwattananuwat
- *Options, Futures, and Other Derivatives* by John Hull
- [Wikipedia: Black-Scholes model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)

