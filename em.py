import numpy as np
from plot_hist import read_y

def normale(y, m, s2):
    return np.exp(-(y-m)**2/(2*s2))/np.sqrt(2*np.pi*s2)

def f_theta(y, pi, mu, s2):
    s = 0
    for i in range(len(pi)):
        s += pi[i]*normale(y, mu[i], s2[i])
    return s

def rho(y, i, pi, mu, s2):
    return pi[i]*normale(y, mu[i], s2[i])/f_theta(y, pi, mu, s2)

def compute_pi_star(y, pi, mu, s2):
    n, N = len(pi), len(y)
    pi_star = np.zeros(n)
    for i in range(n):
        pi_star[i] = np.mean(rho(y, i=i, pi=pi, mu=mu, s2=s2))

    return pi_star

def compute_mu_star(y, pi, mu, s2):
    n, N = len(pi), len(y)
    mu_star = np.zeros(n)
    for i in range(n):
        rho_y = rho(y, i, pi, mu, s2)
        mu_star[i] = np.vdot(rho_y, y)/np.sum(rho_y)

    return mu_star

def compute_s2_star(y, pi, mu, s2, mu_star):
    n, N = len(pi), len(y)
    s2_star = np.zeros(n)
    for i in range(n):
        rho_y = rho(y, i, pi, mu, s2)
        s2_star[i] = np.vdot(rho_y, (y-mu_star[i])**2)/np.sum(rho_y)

    return s2_star

def em(pi=[], mu=[], s2=[]):
    if pi == [] or mu == [] or s2 == []:
        pi=np.array([1./4, 3./4])
        mu=np.array([.57, .67])
        s2=np.array([1./10000, 1./10000])

    y = read_y('crabe.txt')

    # print('\ny :\n{}'.format(y))
    N = len(y)
    N_iter=1000
    theta=np.zeros((5, N+1))

    print('\npi0 :\n{}'.format(pi))
    print('mu0 :\n{}'.format(mu))
    print('s20 :\n{}\n'.format(s2))

    print('\nIteration (out of {}) :'.format(N_iter))
    for k in range(N_iter):
        pi_star = compute_pi_star(y, pi, mu, s2)
        mu_star = compute_mu_star(y, pi, mu, s2)
        s2_star = compute_s2_star(y, pi, mu, s2, mu_star)

        pi = pi_star
        mu = mu_star
        s2 = s2_star

        if (k+1) % (N_iter//10) == 0:
            print('\t'+str(k+1))

    print('\npi :\n{}'.format(pi_star))
    print('mu :\n{}'.format(mu_star))
    print('s2 :\n{}\n'.format(s2_star))

    return pi, mu, s2

if __name__ == '__main__':
    em()