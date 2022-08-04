The Black-Scholes equation: 

$rS\frac{\partial C}{\partial S}+\frac{1}{2}\sigma^2S^2\frac{\partial^2 C}{\partial S^2}+\frac{\partial C}{\partial t} = rC$

where $C$ is the value of a call, $S$ is the stock price, $t$ is time, $\sigma$ is volatility, and $r$ is the interest rate. 

The above equation describes how $S$ and $t$ affect $C$. $\sigma$ and $r$ are not considered variables, but rather inputs which are assumed to remain constant over the life of the option.

Note that $\frac{\partial C}{\partial S}$ is the option's delta $\Delta$, $\frac{\partial^2 C}{\partial S^2}$ is the option's gamma $\Gamma$, and $\frac{\partial C}{\partial t}$ is the option's theta $\Theta$.

