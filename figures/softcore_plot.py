import numpy as np
import matplotlib.pyplot as pl
import pickle

fep_lambdas = np.array([0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
                        0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0])
to_kcal = 0.23900573614
no_sc = pickle.load(open('without_softcore.p','r')) * to_kcal
yes_sc = pickle.load(open('with_softcore.p','r')) * to_kcal
params = {'legend.fontsize': 8}
with pl.rc_context(params):
    fig = pl.figure(figsize=(3.25,3.25))
    ax = fig.add_subplot(111)
    ax.set_xlim(min(fep_lambdas), max(fep_lambdas))
    points = ax.errorbar(fep_lambdas,
                         no_sc[0],
                         yerr = no_sc[1],
                         fmt = '-ro',
                         markersize=4,
                         label='without Coulomb softcore')
    points2 = ax.errorbar(fep_lambdas,
                          yes_sc[0],
                          yerr = yes_sc[1],
                          fmt = '-bo',
                          markersize=4,
                          label='with Coulomb softcore')
    ax.set_xlim(min(fep_lambdas), max(fep_lambdas))
    ax.plot([0,1],[0,0], 'k-', lw=2)
    ax.set_xlabel(r"$\lambda$", fontsize=10)
    ax.set_ylabel(r"$\langle\partial\mathcal{H}/\partial\lambda\rangle$ (kcal$\cdot$mol$^{-1}$)", fontsize=10)
    pl.legend(loc=1)
    pl.tight_layout()
    fig.savefig("TI_plot.pdf")
    pl.close()


# Presentation figure
with pl.rc_context(params):
    fig = pl.figure(figsize=(3.25,3.25))
    ax = fig.add_subplot(111)
    ax.set_xlim(min(fep_lambdas), max(fep_lambdas))
    points = ax.errorbar(fep_lambdas,
                         no_sc[0],
                         yerr = no_sc[1],
                         fmt = '-ro',
                         markersize=4,
                         label='without Coulomb softcore')
    points2 = ax.errorbar(fep_lambdas,
                          yes_sc[0],
                          yerr = yes_sc[1],
                          fmt = '-bo',
                          markersize=4,
                          label='with Coulomb softcore')
    ax.set_xlim(min(fep_lambdas), max(fep_lambdas))
    ax.plot([0,1],[0,0], 'k-', lw=2)
    ax.set_xlabel(r"$\lambda$", fontsize=10)
    ax.set_ylabel(r"$\langle\partial\mathcal{H}/\partial\lambda\rangle$ (kcal$\cdot$mol$^{-1}$)", fontsize=10)
    pl.title(r"methanol $\rightarrow$ methane")
    pl.legend(loc=1)
    pl.tight_layout()
    fig.savefig("TI_plot_presentation.pdf")
    pl.close()




