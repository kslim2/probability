# This is an example of how to apply the
# normalization with the numpy 
from numpy.random import normal 

# define the distribution
mu = 50
sigma = 5
n = 10 

# generate the sample
sample = normal(mu, sigma, n)
print(sample)