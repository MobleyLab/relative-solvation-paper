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


relative = [-0.0144,-6.0911,-5.9687,-2.8337,-3.0686,-8.6737,0.1390,0.1042]
none = [-0.18363,0-6.1476,-6.1539,-2.8950,-3.0719,-8.6157,0.0187,0.0157]
absolute = [0.046,-6.26,-6.21,-2.90,-3.06,-8.57,0.19,0.19]

mue = mue_calculation(relative,absolute)
print("MUE unperturbed hbonds vs absolute:")
print(mue)
mue = mue_calculation(relative,none)
print("MUE unperturbed hbonds vs no constraints:")
print(mue)
#write everything on a file
#outputfile = open("mue_val.dat","w")
#outputfile.write("MUE value: %.4f" % mue)


