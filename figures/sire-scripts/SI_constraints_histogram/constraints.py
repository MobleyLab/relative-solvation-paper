import matplotlib.pyplot as plt
from numpy import *
import math, os, sys, re
import seaborn as sbn
sbn.set_style("whitegrid")
#Here we are going to plot the absolute values along with the relative computed with
#all bond constraints, no constr and hbondsnotpert


#select seaborn color palette to color all the bars
#actually I think blue an red are better for the moment
colors = ["blue","red","orange"]#sbn.,"color_palette("hls",16)
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
#methane ~ethane
methethallb = ax.bar(ind[0],-0.4860,width,color=colors[0],yerr=0.003,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methethnoconstr = ax.bar(ind[0]+width,-0.1863,width,color=colors[1],yerr=0.0413,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methethnohbonds = ax.bar(ind[0]+2*width,-0.0144,width,color=colors[2],yerr=0.0557,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
#ethane ~methanol
ethmetholallb = ax.bar(ind[1],-6.2298,width,color=colors[0],yerr=0.0127,\
                error_kw = dict(elinewidth=2,ecolor="black"))
ethmetholnoconstr = ax.bar(ind[1]+width,-6.1476,width,color=colors[1],yerr=0.0312,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
ethmetholhbonds = ax.bar(ind[1]+2*width,-6.0911,width,color=colors[2],yerr=0.0349,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
#methane ~methanol
methmetholallb = ax.bar(ind[2],-6.0838,width,color=colors[0],yerr=0.0073,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methmetholnoconstr = ax.bar(ind[2]+width,-6.1539,width,color=colors[1],yerr=0.0170,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methmetholhbonds = ax.bar(ind[2]+2*width,-5.9687,width,color=colors[2],yerr=0.0417,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylfuran
meth2mfallb = ax.bar(ind[3],-3.4023,width,color=colors[0],yerr=0.031,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mfnoconstr = ax.bar(ind[3]+width,-2.8950,width,color=colors[1],yerr=0.0637,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mfnohbonds = ax.bar(ind[3]+2*width,-2.8337,width,color=colors[2],yerr=0.0365,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ toluene
methtolallb = ax.bar(ind[4],-3.790,width,color=colors[0],yerr=0.03,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methtolnoconstr = ax.bar(ind[4]+width,-3.0719,width,color=colors[1],yerr=0.0635,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methtolnohbonds = ax.bar(ind[4]+2*width,-3.0686,width,color=colors[2],yerr=0.0217,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ 2methylindole
meth2mindallb = ax.bar(ind[5],-9.150,width,color=colors[0],yerr=0.043,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mindnoconstr = ax.bar(ind[5]+width,-8.6157,width,color=colors[1],yerr=0.0413,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
meth2mindhbonds = ax.bar(ind[5]+2*width,-8.6737,width,color=colors[2],yerr=0.0826,\
                 error_kw = dict(elinewidth=2,ecolor="black"))

#methane ~ neopentane
methneopallb = ax.bar(ind[6],-2.0981,width,color=colors[0],yerr=0.0130,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneopnoconstr = ax.bar(ind[6]+width,0.0187,width,color=colors[1],yerr=0.0618,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneopnohbonds = ax.bar(ind[6]+2*width,0.139,width,color=colors[2],yerr=0.055,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
#methane ~ neopentane2
methneo2pallb= ax.bar(ind[7],-0.486,width,color=colors[0],yerr=0.003,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneo2pnoconstr = ax.bar(ind[7]+width,0.157,width,color=colors[1],yerr=0.0380,\
                 error_kw = dict(elinewidth=2,ecolor="black"))
methneo2phbonds = ax.bar(ind[7]+2*width,0.104,width,color=colors[2],yerr=0.0628,\
                 error_kw = dict(elinewidth=2,ecolor="black"))



#ax.set_ylim()
#plt.yticks(arange(start,end,pace))
#set the fontsize of the y-axis ticks
plt.yticks(fontsize=15)
#set 8 point for the x ticks
plt.xticks(arange(8))
#now I do not put any name on the x ticks, since it may be ok to put molecules
tick_name = ["","","","","","","","","","",""]
#assign the ticks name
xTickMarks=[str(x) for x in tick_name]
#set the size
xtickNames = ax.set_xticklabels(xTickMarks,fontsize=20)

#grid on plot
plt.grid(True)
#legend here we need to fix the labels
ax.legend((methethallb,methethnoconstr,methethnohbonds),("All bonds","None","H bonds not pert"),loc="best",fontsize=20)
#savefigure
plt.savefig("sire_constraints.png",dpi=300,transparent=True)
plt.savefig("sire_constraints.pdf",dpi=300)
