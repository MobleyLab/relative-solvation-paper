import numpy as np
import matplotlib.pyplot as pl
import pickle
import matplotlib.image as image
from matplotlib.cbook import get_sample_data

no_sc = pickle.load(open('without_softcore.p','r'))
yes_sc = pickle.load(open('with_softcore.p','r'))
params = {'legend.fontsize': 8}
with pl.rc_context(params):
    fig = pl.figure(figsize=(3.25,3.25))
    ax = fig.add_subplot(111)
    ax.set_xlim(min(vdw_lambdas), max(vdw_lambdas))
    points = ax.errorbar(vdw_lambdas,
                         no_sc[0],
                         yerr = no_sc[1],
                         fmt = '-ro',
                         markersize=4,
                         label='without Coulomb softcore')
    points2 = ax.errorbar(vdw_lambdas,
                          yes_sc[0],
                          yerr = yes_sc[1],
                          fmt = '-bo',
                          markersize=4,
                          label='with Coulomb softcore')
    ax.set_xlim(min(vdw_lambdas), max(vdw_lambdas))
    ax.plot([0,1],[0,0], 'k-', lw=2)
    ax.set_xlabel(r"$\lambda$", fontsize=10)
    ax.set_ylabel(r"$\langle\partial\mathcal{H}/\partial\lambda\rangle$ (kcal$\cdot$mol$^{-1}$)", fontsize=10)
    pl.legend(loc=1)
    pl.tight_layout()
    fig.savefig("TI_plot.pdf")
    pl.close()


