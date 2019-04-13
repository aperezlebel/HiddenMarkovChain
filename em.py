import numpy as np

pi0=np.array([1./4, 3./4])
pi=pi0
mu=np.array([.57, .67])
s2=np.array([1./10000, 1./10000])

file = open('crabe.txt')

y=.582+.004*np.array(range(29))
print('\ny :\n{}'.format(y))
N = len(y)
N_iter=1000
theta=np.zeros((5, N+1))

print('\npi :\n{}'.format(pi0))
print('mu :\n{}'.format(mu))
print('s2 :\n{}\n'.format(s2))


def normale(y, m, s2):
    return np.exp(-(y-m)**2/(2*s2))/np.sqrt(2*np.pi*s2)

def f_theta(y, pi, mu, s2):
    s = 0
    for i in range(len(pi)):
        s += pi[i]*normale(y, mu[i], s2[i])
    return s

def rho(i, y, pi, mu, s2):
    return pi[i]*normale(y, mu[i], s2[i])/f_theta(y, pi, mu, s2)

def compute_pi_star(pi, mu, s2):
    n = len(pi)
    pi_star = np.zeros(n)
    for i in range(n):
        for k in range(N):
            pi_star[i] += rho(i, y[k], pi, mu, s2)
        pi_star[i] /= N

    return pi_star

def compute_mu_star(pi, mu, s2):
    n = len(pi)
    mu_star = np.zeros(n)
    for i in range(n):
        sum1 = 0.
        for k in range(N):
            sum1 += rho(i, y[k], pi, mu, s2)*y[k]
        sum2 = 0.
        for k in range(N):
            sum2 += rho(i, y[k], pi, mu, s2)
        mu_star[i] = sum1/sum2

    return mu_star

def compute_s2_star(pi, mu, s2, mu_star):
    n = len(pi)
    s2_star = np.zeros(n)
    for i in range(n):
        sum1 = 0.
        for k in range(N):
            sum1 += rho(i, y[k], pi, mu, s2)*(y[k] - mu_star[i])**2
        sum2 = 0.
        for k in range(N):
            sum2 += rho(i, y[k], pi, mu, s2)
        s2_star[i] = sum1/sum2

    return s2_star

print('\nIteration (out of {}) :'.format(N_iter))
for k in range(N_iter):
    pi_star = compute_pi_star(pi, mu, s2)
    mu_star = compute_mu_star(pi, mu, s2)
    s2_star = compute_s2_star(pi, mu, s2, mu_star)

    pi = pi_star
    mu = mu_star
    s2 = s2_star

    if (k+1) % 100 == 0:
        print('\t'+str(k+1))

print('\npi :\n{}'.format(pi_star))
print('mu :\n{}'.format(mu_star))
print('s2 :\n{}\n'.format(s2_star))
