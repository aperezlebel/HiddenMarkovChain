from matplotlib import pyplot as plt

def plot_hist(fichier):
    data_crabe = open(fichier)
    X = []
    value = 0.580
    for line in data_crabe:
        for i in range(int(line.strip('\n'))):
            X.append(value)
        value+=0.004
    data_crabe.close()


    n, bins, patches = plt.hist(X, 29, density=True, facecolor='g')
    bins = bins/1000
    plt.ylabel('Probability')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    plot_hist('crabe.txt')