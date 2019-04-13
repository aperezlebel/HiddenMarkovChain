# Estimating the mixing law of Weldon's crab with Expectation-Maximisation algorithm

## Weldon's crab data

The data is contained in the crabe.txt file. Plot the empirical law and it's approximation by a gaussian by running :

```
python plot_hist.py
```

## Mixing law

We suppose that the population was divided into two groups before the mixing. Each population has is own law, approximated by a gaussian.

Get the gaussians' parameters of each population by running :

```
python em.py
```

Plot the recovered mixing law and compare it to the the first gaussian approximation by running :

```
python main.py
```

It also plots the results under the hypothesis of 3 initial populations.

## Resource

This work has been carried out following the subject.pdf file, proposed by the ENPC school. Please see more details in it.
