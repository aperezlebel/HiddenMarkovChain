from scipy.stats import chisquare, norm
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from numpy.random import normal

file = open('crabe.txt', 'r')

# f_obs = []
f_obs = np.empty(0)
k=0

total = 0
for line in file:
    nb = int(line.strip('\n'))
    for i in range(nb):
        f_obs = np.append(f_obs, 0.582+0.004*k)
    k += 1
    total += nb
    # f_obs.append(int(line.strip('\n')))

# f_obs = f_obs/np.sum(f_obs)
mean, std = norm.fit(f_obs)
print(mean)
print(std)
# X = np.linspace(0.582, 0.694, total)
# f_gaussian = norm.pdf(X, mean, std)

f_gaussian = normal(mean, std, len(f_obs))


print('\nObserved frequencies :\n{}\n'.format(f_obs))
print('\nGaussian frequencies :\n{}\n'.format(f_gaussian))

print(mean)
print(std)

# plt.plot(X, f_obs)
# plt.plot(X, f_gaussian)
# plt.show()


print(chisquare(f_obs, f_gaussian))
