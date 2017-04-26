import math

def mue_calculation(list1,list2):
    mue = 0.0
    counter = 0
    for i,val in enumerate(list1):
        mean = abs(val - list2[i])
        mue +=mean
        counter +=1
    mue = mue/counter
    return mue

relative = [-0.04860,-6.2298,-6.0838,-3.4023,-3.7907,-9.1503,-2.0981,-0.4860]
absolute = [0.046,-6.26,-6.21,-2.90,-3.06,-8.57,0.19,0.19]
mue = mue_calculation(relative,absolute)
print(mue)

#write everything on a file
outputfile = open("mue_val.dat","w")
outputfile.write("MUE value: %.4f" % mue)


