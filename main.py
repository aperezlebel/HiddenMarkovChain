from plot_hist import plot_hist
from em import em

pi, mu, s2 = em()
plot_hist('crabe.txt', mu, s2, pi)
