import numpy as np
from plot_hist import plot_hist
from em import em

# Valeurs initiales pour 2 populations
pi0_2=np.array([1./4, 3./4])
mu0_2=np.array([.57, .67])
s20_2=np.array([1./10000, 1./10000])

# Valeurs initiales pour 3 populations
pi0_3=np.array([1./3, 1/3, 1./3])
mu0_3=np.array([.57, .6, .67])
s20_3=np.array([1./10000, 1./10000, 1./10000])


# Loi empirique
plot_hist('crabe.txt')

# 2 populations
pi, mu, s2 = em(pi0_2, mu0_2, s20_2)
plot_hist('crabe.txt', mu, s2, pi)

# 3 populations
pi, mu, s2 = em(pi0_3, mu0_3, s20_3)
plot_hist('crabe.txt', mu, s2, pi)
