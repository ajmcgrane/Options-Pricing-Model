import numpy as np 

s0 = 100 # Intial price
k = 100 # Strike price
t = 0 # Time to expire in years
n = 5 # Number of steps
r = 0.05 # Risk free rate
sigma = 0.2 # Volitility

def binomial_option_price_tree(s0, k, t, r, sigma, n):
    delta = t/n # Size of each step
    u = np.exp(sigma * np.sqrt(delta)) # Up
    d = 1 / u # Down
    p = (np.exp(r * delta) - d) / (u - d) # Risk neutral probabilty

    # Initialize asset prices at maturity
    S = np.zeros(n+1) 
    for i in range(n+1): 
        S[i] = s0 * (u ** (n-1)) * (d ** i)
    
    # Intialize option values at maturity
    V = np.zeros(n+1)
    for i in range(n+1):
        V[i] = max(S[i] - k, 0)
    
    # Iritiate backwards through tree
    for i in range(n-1, -1, -1):
        for j in range(i+1):
            V[j] = np.exp(-r * delta) * (p * V[j] + (1 - p) * V[j + 1])
            S[j] = s0 * (u ** (i - j)) * (d ** j)
            V[j] = max(V[j], S[j] - k)

    return V[0]

price = binomial_option_price_tree(s0, k, t, r, sigma, n)

print(price)
