#Puntual calculation for R and MUE
import math
import sys
import scipy.stats

def mue_calculation(list1,list2):
    mue = 0.0
    counter = 0
    for i,val in enumerate(list1):
        mean = abs(val - list2[i])
        mue +=mean
        counter +=1
    mue = mue/counter
    return mue

def calculate_R2 ( list1, list2 ):
    r_value,p = scipy.stats.pearsonr(list1,list2)

    return r_value**2, r_value



###MAIN###
exp = open(sys.argv[1],"r").readlines()
rel = open(sys.argv[2],"r").readlines()

relative = []

for line in exp:
    val = line.split(",")[1]
    relative.append(float(val))

absolute = []

for line in rel:
    val = line.split(",")[1]
    absolute.append(float(val))



mue = mue_calculation(relative,absolute)
print("MUE")
print(mue)
r2,r = calculate_R2(relative,absolute)
print("R2")
print(r2)
#write everything on a file
outputfile = open("mue_val.dat","w")
outputfile.write("MUE value: %.4f" % mue)
outputfile.write("R   value: %.4f" % r)
outputfile.write("R2  value: %.4f" % r2)
