Black Scholes 
====
## The Equation
The Black-Scholes differential equation (the solution to which yields the Black-Scholes model) is given by:

$rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2 C}{\partial S^2}+\frac{\partial C}{\partial t} = rC$

where $C$ is the value of a call, $S$ is the stock price, $t$ is time, $\sigma$ is volatility, and $r$ is the interest rate. 

The above equation describes how $S$ and $t$ affect $C$. $\sigma$ and $r$ are not considered variables, but rather inputs which are assumed to remain constant over the life of the option.

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

Using $\Delta_{avg}$ the price change of the option should be approximately

$(S_2-S_1)\Delta_{avg} = (S_2-S_1)\Delta + \frac{1}{2}(S_2-S_1)^2\Gamma$

Reminding ourselves that $\Delta=\frac{\partial C}{\partial S}$ and $\Gamma=\frac{\partial^2 C}{\partial S^2}$, this looks awfully similar to the first two terms of the Black-Scholes equation, $rS\Delta+\frac{1}{2}\sigma^2S^2\Gamma$. 

The primary differences between the equations are the interest-rate component attached to $S$ and the volatility component attached to gamma. The Black-Scholes equation assumes an instantaneous price change instead of a discrete price change. 

## Sources
- *Option Volatility and Pricing, Chapter 18: The Black-Scholes Model* by Sheldon Natenberg
- [Wikipedia: Black-Scholes Equation](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_equation)