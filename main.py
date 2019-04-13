import numpy as np
from plot_hist import plot_hist
from em import em


pi0=np.array([1./4, 1/2, 3./4])
mu0=np.array([.57, .6, .67])
s20=np.array([1./10000, 1./10000, 1./10000])

# 2 populations
pi, mu, s2 = em()
plot_hist('crabe.txt', mu, s2, pi)

# 3 populations
pi, mu, s2 = em(pi0, mu0, s20)
plot_hist('crabe.txt', mu, s2, pi)
