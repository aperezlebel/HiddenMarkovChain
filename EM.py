from math import sqrt, pi, exp

def f(mu, sigma, yk):
    return 1./sqrt(2*pi*sigma**2)*exp(-(yk-mu)**2/(2*sigma**2))

def EM(list_of_y_k):
    # Initialisation
    pi = [1./4, 3./4]
    mu = [.57, .67]
    sigma = [1./10000, 1./10000]
    theta = [mu, sigma]
    N_iter = 1000
    N = len(list_of_y_k)
    pi_aux = [0, 0]

    for _ in range(N_iter):
        for j in range(2):
            s = 0
            for k in range(N):
                rho_i_k = pi[j]*f(mu[j], sigma[j], list_of_y_k[k])/(pi[0]*f(mu[0], sigma[0], list_of_y_k[k])+pi[1]*f(mu[1], sigma[1], list_of_y_k[k]))
                s += rho_i_k
            pi_aux[j] = 1./N*s
        pi = pi_aux[:]
        

    return True

if __name__=='__main__':
    print(f(0.5, 1, 1))