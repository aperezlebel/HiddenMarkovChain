from matplotlib import pyplot as plt
from scipy import stats, signal
import numpy as np
from math import floor
from scipy.integrate import quad    
import numpy as np

def gaussian(y, mu, s2, pi=1):
    return pi*np.exp(-(y-mu)**2/(2*s2))/np.sqrt(2*np.pi*s2)

def read_y(file_name):
    data_crabe = open(file_name)
    y = []
    value = 0.580
    for line in data_crabe:
        freq = int(line.strip('\n'))
        for i in range(freq):
            y.append(value)
        value+=0.004
    data_crabe.close()

    return np.array(y)

def get_freqs(file_name):
    data_crabe = open(file_name)
    freqs = []
    for line in data_crabe:
        freqs.append(int(line.strip('\n')))
    data_crabe.close()
    return np.array(freqs)

def get_theoretical_frequencies(gaussians, Mu, Sigma2, Pi):

    def function(x): 
        s = 0.
        for i in range(len(Mu)):
            s += Pi[i]*gaussian(x, Mu[i], Sigma2[i])
        return s
    
    frequencies = []
    xmin = 0.580
    for i in range(29):
        xmax = xmin + 0.004
        res, err = quad(function, xmin, xmax)
        frequencies.append(res*1000)
        xmin = xmax

    return frequencies


def plot_hist(fichier, Mu = [], S2 = [], Pi = []):
    '''
        Plot the data law, its gaussian approximation and
        plot as many gaussian as (mu, s2) in Mu and S2 where
        mu : gaussian's mean
        s2 : squared std
    '''
    
    y = read_y(fichier)
    freqs = get_freqs(fichier)

    if Mu==[] or S2==[] or Pi==[]:
        k2, p = stats.normaltest(y)
        print("Test du Chi2 : Statistic=" + str(k2) + ", p-value=" + str(p))

    (mu, sigma) = stats.norm.fit(y)
    n, bins, patches = plt.hist(y, 29, density=True, facecolor='g')

    X = np.linspace(bins[0], bins[-1], 100)
    X_chi2 = np.linspace((bins[0]+bins[1])/2, (bins[-2]+bins[-1])/2, 29) 
    v_gaussian = np.vectorize(gaussian)
    plt.plot(X, v_gaussian(X, mu, sigma**2), linewidth=2, color='r', label='Fitted gaussian')

    assert(len(Mu) == len(S2) and len(Mu) == len(Pi))
    gaussians = []
    gaussians_chi_square = []
    tirages = []
    for i in range(len(Mu)):
        gaussians.append(v_gaussian(X, Mu[i], S2[i], Pi[i]))
        gaussians_chi_square.append(v_gaussian(X_chi2, Mu[i], S2[i], Pi[i]))
        plt.plot(X, gaussians[-1], label='Gaussian population '+str(i+1))

    if len(gaussians) > 0:
        plt.plot(X, np.sum(gaussians, axis=0), label='Sum of all gaussians', linewidth=2, color='b')
        real_frequencies = get_theoretical_frequencies(gaussians_chi_square, Mu, S2, Pi)
        chisq, p_value = stats.chisquare(freqs, real_frequencies)
        print("Test du Chi2 : Statistic=" + str(chisq) + ", p-value=" + str(p_value))

    plt.ylabel('Probability')
    plt.title('Histogram')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__=='__main__':
    plot_hist('crabe.txt')
