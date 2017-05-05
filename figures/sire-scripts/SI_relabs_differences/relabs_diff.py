import matplotlib.pyplot as plt
from numpy import *
import math, os, sys, re
import seaborn as sbn
sbn.set_style("whitegrid")
#Here we are going to plot the absolute values along with the relative computed with
#all bond constraints
#all the values are taken from the google spreadsheet


#select seaborn color palette to color all the bars
#actually I think blue an red are better for the moment
colors = ["blue","red"]#sbn.color_palette("hls",16)
#now create a list of number to locate all the free energies
#we will have on the x-axis the molecule - to be modified in powerpoint -
#on the y-axis the transformation starting from methane
#so we will have : met~eth, eth~methOL, meth~methOL,meth~2MF,meth~tol,meth~2MIND,meth~neoP
ind = arange(8) - 0.25 #add a -0.25 so we center the plot
#width of each bar
width = 0.25 #which is the same as the spacing
fig = plt.figure(figsize=[10,7])
ax = fig.add_subplot(111)

#BARS:
#methane ~ethane A
methethrel = ax.bar(ind[0],-0.4860,width,color=colors[0],yerr=0.003,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methethabs = ax.bar(ind[0]+width,-0.046,width,color=colors[1],yerr=0.021,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
#ethane ~methanol B
ethmetholrel = ax.bar(ind[1],-6.2298,width,color=colors[0],yerr=0.0127,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
ethmetholabs = ax.bar(ind[1]+width,-6.26,width,color=colors[1],yerr=0.051,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~methanol C
methmetholrel = ax.bar(ind[2],-6.0838,width,color=colors[0],yerr=0.0073,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methmetholabs = ax.bar(ind[2]+width,-6.21,width,color=colors[1],yerr=0.055,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylfuran D
meth2mfrel = ax.bar(ind[3],-3.4023,width,color=colors[0],yerr=0.031,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mfabs = ax.bar(ind[3]+width,-2.903,width,color=colors[1],yerr=0.029,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ toluene E
methtolrel = ax.bar(ind[4],-3.790,width,color=colors[0],yerr=0.03,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methtolabs = ax.bar(ind[4]+width,-3.065,width,color=colors[1],yerr=0.031,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylindole F
meth2mindrel = ax.bar(ind[5],-9.150,width,color=colors[0],yerr=0.043,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mindabs = ax.bar(ind[5]+width,-8.571,width,color=colors[1],yerr=0.029,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ neopentane G
methneoprel = ax.bar(ind[6],-2.0981,width,color=colors[0],yerr=0.0130,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneopabs = ax.bar(ind[6]+width,-0.190,width,color=colors[1],yerr=0.060,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ neopentane2 H
methneo2prel = ax.bar(ind[7],-0.486,width,color=colors[0],yerr=0.003,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneo2pabs = ax.bar(ind[7]+width,-0.190,width,color=colors[1],yerr=0.060,\
                 error_kw = dict(elinewidth=2,ecolor="black"))



#ax.set_ylim()
#plt.yticks(arange(start,end,pace))
#set the fontsize of the y-axis ticks
plt.yticks(fontsize=15)
ax.set_ylabel("$\Delta\Delta G$ / kcal mol$^{-1}$", fontsize=20)
#set 8 point for the x ticks
plt.xticks(arange(8))

tick_name = ["A","B","C","D","E","F","G","H"]
#assign the ticks name
xTickMarks=[str(x) for x in tick_name]
xtickNames = ax.set_xticklabels(xTickMarks)
ax.xaxis.tick_top()
#remember to first put the labels on top of the plot and then fontsize
#otherwise it won't work- it may be a bug in matplotlib
plt.xticks(fontsize=20)
#grid on plot
plt.grid(True)
#legend here we need to fix the labels
ax.legend((methethrel,methethabs),("RAFE $\Delta\Delta G$","RAFE $\Delta\Delta G$ from absolute"),loc="best",fontsize=20)
#savefigure
plt.savefig("SI_sire_allbonds_relabs.png",dpi=300,transparent=True)
plt.savefig("SI_sire_allbonds_relabs.pdf",dpi=300)
