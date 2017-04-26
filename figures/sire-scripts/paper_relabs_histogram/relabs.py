import matplotlib.pyplot as plt
from numpy import *
import math, os, sys, re
import seaborn as sbn
sbn.set_style("whitegrid")

#select seaborn color palette to color all the bars
colors =["blue","red"] #sbn.color_palette("hls",16)
#now create a list of number to locate all the free energies
#we will have on the x-axis the molecule - to be modified in powerpoint -
#on the y-axis the transformation starting from methane
#so we will have : met~eth, eth~methOL, meth~methOL,meth~2MF,meth~tol,meth~2MIND,meth~neoP,2~7
ind = arange(8) - 0.25 #add a -0.25 so we center the plot
#width of each bar
width = 0.25 #which is the same as the spacing
fig = plt.figure(figsize=[10,7])
ax = fig.add_subplot(111)

#BARS:
#methane ~ethane A
methethrel = ax.bar(ind[0],-0.014,width,color=colors[0],yerr=0.056,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methethabs = ax.bar(ind[0]+width,-0.046,width,color=colors[1],yerr=0.021,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
#ethane ~methanol B
ethmetholrel = ax.bar(ind[1],-6.091,width,color=colors[0],yerr=0.035,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
ethmetholabs = ax.bar(ind[1]+width,-6.26,width,color=colors[1],yerr=0.051,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~methanol C
methmetholrel = ax.bar(ind[2],-5.969,width,color=colors[0],yerr=0.042,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methmetholabs = ax.bar(ind[2]+width,-6.21,width,color=colors[1],yerr=0.055,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylfuran D
meth2mfrel = ax.bar(ind[3],-2.834,width,color=colors[0],yerr=0.037,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mfabs = ax.bar(ind[3]+width,-2.903,width,color=colors[1],yerr=0.029,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ toluene E
methtolrel = ax.bar(ind[4],-3.069,width,color=colors[0],yerr=0.022,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methtolabs = ax.bar(ind[4]+width,-3.065,width,color=colors[1],yerr=0.031,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylindole F
meth2mindrel = ax.bar(ind[5],-8.674,width,color=colors[0],yerr=0.083,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mindabs = ax.bar(ind[5]+width,-8.571,width,color=colors[1],yerr=0.029,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ neopentane G
methneoprel = ax.bar(ind[6],-0.139,width,color=colors[0],yerr=0.055,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneopabs = ax.bar(ind[6]+width,-0.190,width,color=colors[1],yerr=0.060,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#2~7 H
cycloprel = ax.bar(ind[7],-0.116,width,color=colors[0],yerr=0.077,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
cyclopabs = ax.bar(ind[7]+width,-0.08,width,color=colors[1],yerr=0.142,\
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
#set the size
xtickNames = ax.set_xticklabels(xTickMarks)
ax.xaxis.tick_top()
#remember to first put the labels on top of the plot and then fontsize
#otherwise it won't work- it may be a bug in matplotlib
plt.xticks(fontsize=20)
#now set the ab,c,d,e,f,g,h on top of the plot
#ax.xaxis.set_label_position("top")
#grid on plot
plt.grid(True)
#legend here we need to fix the labels
ax.legend((methethrel,methethabs),("RAFE $\Delta\Delta G$","RAFE $\Delta\Delta G$ from absolute"),loc="best",fontsize=20)
#savefigure
plt.savefig("sire_histogram.png",dpi=300,transparent=True)
plt.savefig("sire_histogram.pdf",dpi=300)
