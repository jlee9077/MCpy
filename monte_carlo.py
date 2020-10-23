import math
import random
import pylab
from random import gauss
import matplotlib
import matplotlib.pyplot as plt
from numpy import *

#num - number of simulations
#ttm - Time to Maturity
#vol - Volatility
#price - Current Stock Price
#strike - Option Strike Price

def monte_carlo_simulator(num, ttm, vol, price, strike):
    delta = ttm * 252
    data_points = random.randn(delta) * vol / sqrt(delta)
    plt.hist(data_points)
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")

    random_walk = cumprod(1 + random.randn(num, delta) * vol / sqrt(delta), 1) * price
    plt.plot(random_walk)
    plt.show()
    plt.title("Geometric Random Walk")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")

    for point in random_walk:
      plt.plot(point)
    plt.show()
    plt.hist(random_walk[:,-1],40)
    plt.show()
    option_payoff = (random_walk[:,-1] - 100) * ((random_walk[:,-1] - 100) > 0)
    price = mean(option_payoff)
    print(price)

monte_carlo_simulator(1000,2,0.41,280,285)

