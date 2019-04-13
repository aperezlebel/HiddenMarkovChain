import numpy as np

def normale(y, m, s2):
    return np.exp(-(y-m)**2/(2*s2))/np.sqrt(2*np.pi*s2)

def f_theta(y, pi, mu, s2):
    s = 0
    for i in range(len(pi)):
        s += pi[i]*normale(y, mu[i], s2[i])
    return s

def rho(y, i, pi, mu, s2):
    return pi[i]*normale(y, mu[i], s2[i])/f_theta(y, pi, mu, s2)

# v_rho = np.vectorize(rho, excluded=['i', 'pi', 'mu', 's2'])

def compute_pi_star(y, pi, mu, s2):
    n, N = len(pi), len(y)
    pi_star = np.zeros(n)
    for i in range(n):
        # for k in range(N):
        #     pi_star[i] += rho(y[k], i, pi, mu, s2)
        # # print(v_rho(y, i=i, pi=pi, mu=mu, s2=s2))
        # pi_star[i] /= N
        pi_star[i] = np.mean(rho(y, i=i, pi=pi, mu=mu, s2=s2))

    return pi_star

def compute_mu_star(y, pi, mu, s2):
    n, N = len(pi), len(y)
    mu_star = np.zeros(n)
    for i in range(n):
        # sum1 = 0.
        # for k in range(N):
        #     sum1 += rho(y[k], i, pi, mu, s2)*y[k]
        # rho_y = v_rho(y, i=i, pi=pi, mu=mu, s2=s2)
        rho_y = rho(y, i, pi, mu, s2)
        sum1 = np.vdot(rho_y, y)
        # sum2 = 0.
        # for k in range(N):
        #     sum2 += rho(y[k], i, pi, mu, s2)
        sum2 = np.sum(rho_y)
        mu_star[i] = sum1/sum2

    return mu_star

def compute_s2_star(y, pi, mu, s2, mu_star):
    n, N = len(pi), len(y)
    s2_star = np.zeros(n)
    for i in range(n):
        # sum1 = 0.
        # for k in range(N):
        #     sum1 += rho(y[k], i, pi, mu, s2)*(y[k] - mu_star[i])**2
        rho_y = rho(y, i, pi, mu, s2)
        sum1 = np.vdot(rho_y, (y-mu_star[i])**2)
        # sum2 = 0.
        # for k in range(N):
        #     sum2 += rho(y[k], i, pi, mu, s2)
        sum2 = np.sum(rho_y)
        s2_star[i] = sum1/sum2

    return s2_star

def em():
    pi0=np.array([1./4, 3./4])
    pi=pi0
    mu=np.array([.57, .67])
    s2=np.array([1./10000, 1./10000])

    file = open('crabe.txt')

    # Building y vector while reading file
    y = []
    value = 0.582
    for line in file:
        for i in range(int(line.strip('\n'))):
            y.append(value)
        value+=0.004
    # y=.582+.004*np.array(range(29))
    y = np.array(y)

    print('\ny :\n{}'.format(y))
    N = len(y)
    N_iter=10000
    theta=np.zeros((5, N+1))

    print('\npi :\n{}'.format(pi0))
    print('mu :\n{}'.format(mu))
    print('s2 :\n{}\n'.format(s2))

    print('\nIteration (out of {}) :'.format(N_iter))
    for k in range(N_iter):
        pi_star = compute_pi_star(y, pi, mu, s2)
        mu_star = compute_mu_star(y, pi, mu, s2)
        s2_star = compute_s2_star(y, pi, mu, s2, mu_star)

        pi = pi_star
        mu = mu_star
        s2 = s2_star

        if (k+1) % 100 == 0:
            print('\t'+str(k+1))

    print('\npi :\n{}'.format(pi_star))
    print('mu :\n{}'.format(mu_star))
    print('s2 :\n{}\n'.format(s2_star))

    return pi, mu, s2

if __name__ == '__main__':
    em()
